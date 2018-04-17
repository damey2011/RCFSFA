from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.api.serializers import UserDetailSerializer
from programs.models import Programme, ProgramInterestedAttendees


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = '__all__'


class ProgrammeInterestedAttendeeSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    programme = serializers.CharField(source='programme.title')
    user_id = serializers.PrimaryKeyRelatedField(source='user', write_only=True, queryset=User.objects.all())
    programme_id = serializers.PrimaryKeyRelatedField(source='programme', write_only=True, queryset=Programme.objects.all())

    class Meta:
        model = ProgramInterestedAttendees
        fields = (
            'user',
            'programme'
        )
