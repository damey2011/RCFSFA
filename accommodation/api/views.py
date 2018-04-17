from django.shortcuts import render

# Create your views here.
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView

from accommodation.api.pagination import AccommodationPagination
from accommodation.api.serializers import AccommodationSerializer
from accommodation.models import Accommodation


class ListCreateAccommodation(ListCreateAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
    pagination_class = AccommodationPagination
    filter_backends = (SearchFilter,)
