from rest_framework import serializers

from forums.models import Thread


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = (
            'title',
            'author',
            'content',
            'isCommentEnabled',
            'created',
            'lastModified'
        )
