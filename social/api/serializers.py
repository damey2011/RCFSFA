from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.api.serializers import UserDetailSerializer
from social.models import FeedPost, Comment, PostLike, CommentLike, ConversationReplies


class FeedPostSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    like_status = serializers.SerializerMethodField()
    delete_like = serializers.SerializerMethodField()

    class Meta:
        model = FeedPost
        fields = (
            'id',
            'user',
            'post',
            'timestamp',
            'modified',
            'likes',
            'comments',
            'comments_count',
            'like_status',
            'delete_like'
        )

    def get_likes(self, obj):
        return obj.get_like_count()

    def get_comments(self, obj):
        return obj.get_comments()

    def get_comments_count(self, obj):
        return obj.get_comments_count()

    def get_like_status(self, obj):
        if isinstance(self.context['request'].user, User):
            return PostLike.objects.filter(user=self.context['request'].user, post=obj).exists()
        else:
            return False

    def get_delete_like(self, obj):
        if isinstance(self.context['request'].user, User):
            if PostLike.objects.filter(user=self.context['request'].user, post=obj).exists():
                pk = PostLike.objects.filter(user=self.context['request'].user, post=obj).first().id
                return reverse('retrieve-update-delete-post-like', kwargs={'pk': pk})
            else:
                return ""
        else:
            return ""

    def validate(self, attrs):
        user = self.context['request'].user
        if isinstance(user, User):
            return attrs
        raise ValidationError('User is not Authenticated or Invalid')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        fp = FeedPost.objects.create(**validated_data)
        return fp


class SimpleFeedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPost
        fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    post = SimpleFeedPostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(source='post', write_only=True, queryset=FeedPost.objects.all(),
                                                 default=FeedPost.objects.first())
    children_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content',
            'post',
            'post_id',
            'timestamp',
            'modified',
            'likes',
            'children',
            'children_count'
        )

    def get_likes(self, obj):
        return obj.get_like_count()

    def get_children(self, obj):
        return obj.get_children()

    def get_children_count(self, obj):
        return obj.get_children_count()

    def validate(self, attrs):
        user = self.context['request'].user
        if isinstance(user,
                      User):  # We are trying to check here if the accessing user is not an anonymous user (object)
            return attrs
        raise ValidationError('User is not Authenticated or Invalid')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        parent = self.context['view'].kwargs.get('parent', None)
        post = self.context['view'].kwargs.get('pk', None)

        if parent is not None:
            validated_data['parent'] = parent
        elif post is not None:
            validated_data['post_id'] = post
            validated_data['post'] = FeedPost.objects.get(pk=post)

        comment = Comment.objects.create(**validated_data)
        return comment


class CommentCommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    children_count = serializers.SerializerMethodField(read_only=True)
    children = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'parent',
            'content',
            'children',
            'children_count',
            'timestamp',
            'likes',
            'modified',
        )

    def get_children(self, obj):
        return obj.get_children()

    def get_children_count(self, obj):
        return obj.get_children_count()

    def get_likes(self, obj):
        return obj.get_like_count()


class GeneralCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostLikeSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PostLike
        fields = (
            'id',
            'user',
            'post'
        )

    def validate(self, attrs):
        user = self.context['request'].user
        if isinstance(user, User):
            return attrs
        raise ValidationError('User is not Authenticated or Invalid')

    def create(self, validated_data):
        if PostLike.objects.filter(user=self.context['request'].user,
                                   post_id=self.context['view'].kwargs.get('pk', None)).exists():
            raise ValidationError('You can\'t like this post more than once')

        validated_data['user'] = self.context['request'].user
        validated_data['post_id'] = self.context['view'].kwargs['pk']
        postlike = PostLike.objects.create(**validated_data)
        return postlike


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        if isinstance(user, User):
            return attrs
        raise ValidationError('User is not Authenticated or Invalid')

    def create(self, validated_data):
        user = self.context['request'].user
        if CommentLike.objects.filter(user=user, comment_id=self.context['view'].kwargs['pk']).exists():
            return ValidationError("This comment has already been liked by you!")
        validated_data['user'] = self.context['request'].user
        validated_data['post_id'] = self.context['view'].kwargs['pk']
        comment_like = CommentLike.objects.create(**validated_data)
        return comment_like


class MessageSerializer(serializers.ModelSerializer):
    conv = serializers.PrimaryKeyRelatedField(read_only=True)
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ConversationReplies
        fields = (
            'id',
            'user',
            'reply',
            'time',
            'read'
        )

    def validate(self, attrs):
        user = self.context['request'].user
        if isinstance(user, User):
            return attrs
        raise ValidationError('User is not Authenticated or Invalid')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        validated_data['conv'] = self.context['view'].kwargs.get('pk', None)
        c = ConversationReplies.objects.create(**validated_data)
        return c
