from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField

from accounts.models import MemberProfile, ExcoProfile, CoordinatorProfile, create_profile, UserRole, UserFollowing
from campus.api.serializers import SchoolSerializer
from campus.models import School


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_type = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'user_type'
        )

    def validate(self, attrs):
        email = attrs['email']
        username = attrs['username']

        # Check the token Later If needed, For now accounts be created via regular django

        # Checks if the user already exist
        if User.objects.filter(email=email).exists():
            raise ValidationError("The email address already exist!")
        if User.objects.filter(username=username).exists():
            raise ValidationError("The username already exist!")

        return attrs

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        user_type = validated_data.get('user_type', 0)

        u = User(email=email, username=username, first_name=first_name, last_name=last_name)
        u.set_password(password)
        u.save()

        create_profile(u, user_type)

        return u


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'full_name',
            'picture'
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_picture(self, obj):
        role = UserRole.objects.get(user=obj).role
        host = 'http://'+self.context['request'].get_host()

        if role == 0:
            return host + MemberProfile.objects.get(user=obj).picture.url
        if role == 1:
            return host + CoordinatorProfile.objects.get(user=obj).picture.url
        if role == 2:
            return host + ExcoProfile.objects.get(user=obj).picture.url
        return ''


class MightKnowSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    picture = serializers.SerializerMethodField()
    following_status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'full_name',
            'picture',
            'following_status'
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_picture(self, obj):
        role = UserRole.objects.get(user=obj).role
        host = 'http://'+self.context['request'].get_host()

        if role == 0:
            return host + MemberProfile.objects.get(user=obj).picture.url
        if role == 1:
            return host + CoordinatorProfile.objects.get(user=obj).picture.url
        if role == 2:
            return host + ExcoProfile.objects.get(user=obj).picture.url
        return ''

    def get_following_status(self, obj):
        if isinstance(self.context['request'].user, User):
            return UserFollowing.objects.filter(user=self.context['request'].user, follows=obj).exists()
        else:
            return False


class CreateUserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = '__all__'


class MemberProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    school = SchoolSerializer(read_only=True)
    user_id = PrimaryKeyRelatedField(source='user', write_only=True, queryset=User.objects.all())
    school_id = PrimaryKeyRelatedField(source='school', write_only=True, queryset=School.objects.all())
    gradDegreeClass = serializers.CharField(source='get_gradDegreeClass_display')
    follower_count = serializers.CharField()
    following_count = serializers.CharField()
    posts_count = serializers.CharField()

    class Meta:
        model = MemberProfile
        fields = [
            'user_id',
            'user',
            'school',
            'user_id',
            'school_id',
            'gradYear',
            'gradDegreeClass',
            'course',
            'resAddr',
            'resState',
            'permAddr',
            'permState',
            'phone1',
            'phone2',
            'picture',
            'fbProfile',
            'twProfile',
            'lnkProfile',
            'created',
            'lastModified',
            'follower_count',
            'following_count',
            'posts_count'
        ]


class CoordinatorProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    follower_count = serializers.CharField()
    following_count = serializers.CharField()

    class Meta:
        model = CoordinatorProfile
        fields = (
            'user',
            'job_description',
            'date_of_birth',
            'area_or_zonal',
            'zone',
            'area',
            'picture',
            'follower_count',
            'following_count'
        )


class ExcoProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    follower_count = serializers.CharField()
    following_count = serializers.CharField()

    class Meta:
        model = ExcoProfile
        fields = (
            'user',
            'job_description',
            'date_of_birth',
            'area_or_zonal',
            'zone',
            'area',
            'picture',
            'follower_count',
            'following_count'
        )
