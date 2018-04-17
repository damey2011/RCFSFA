from rest_framework import serializers

from accommodation.models import Accommodation


class AccommodationSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Accommodation
        fields = (
            'id',
            'name',
            'location',
            'town',
            'state',
            'country',
            'images'
        )

    def get_images(self, obj):
        return obj.images
