from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField

from accounts.models import StudentProfile
from campus.api.serializers import SchoolSerializer
from campus.models import School


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email'
        )

    def validate(self, attrs):
        email = attrs['email']
        username = attrs['username']

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
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        u = User(email=email, username=username, first_name=first_name, last_name=last_name)
        u.set_password(password)
        u.save()
        return u


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name'
        ]


class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    school = SchoolSerializer(read_only=True)
    user_id = PrimaryKeyRelatedField(source='user', write_only=True, queryset=User.objects.all())
    school_id = PrimaryKeyRelatedField(source='school', write_only=True, queryset=School.objects.all())
    gradDegreeClass = serializers.CharField(source='get_gradDegreeClass_display')

    class Meta:
        model = StudentProfile
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
            'lastModified'
        ]
