from django.contrib.auth.models import User
from rest_framework import serializers

from forums.models import Thread, Comment, ChildComment, Like
from accounts.api.serializers import UserDetailSerializer


class ThreadSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(source='author', queryset=User.objects.all(), write_only=True)
    comments_count = serializers.SerializerMethodField()
    comments_url = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = (
            'id',
            'title',
            'author_id',
            'author',
            'content',
            'isCommentEnabled',
            'created',
            'lastModified',
            'comments_count',
            'comments_url',
            'likes'
        )
        read_only_fields = [
            'author'
        ]

    def get_comments_count(self, obj):
        return obj.get_comments_count()

    def get_comments_url(self, obj):
        return obj.get_comments_url()

    def get_likes(self, obj):
        return obj.get_like_count()


class CommentSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', queryset=User.objects.all(), write_only=True)
    comments_count = serializers.SerializerMethodField()
    comments_url = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'author_id',
            'author',
            'parent',
            'timestamp',
            'last_modified',
            'content',
            'comments_count',
            'comments_url'
        )
        read_only_fields = [
            'author'
        ]

    def get_comments_count(self, obj):
        return obj.get_comments_count()

    def get_comments_url(self, obj):
        return obj.get_comments_url()


class ChildCommentSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', queryset=User.objects.all(), write_only=True)
    comments_count = serializers.SerializerMethodField()
    comments_url = serializers.SerializerMethodField()

    class Meta:
        model = ChildComment
        fields = (
            'id',
            'author_id',
            'author',
            'parent',
            'timestamp',
            'last_modified',
            'content',
            'comments_count',
            'comments_url'
        )
        read_only_fields = [
            'author',
            'parent'
        ]

    def get_comments_count(self, obj):
        return obj.get_comments_count()

    def get_comments_url(self, obj):
        return obj.get_comments_url()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id',
            'author',
            'type',
            'parent'
        )
