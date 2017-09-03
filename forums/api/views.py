from rest_framework.generics import ListCreateAPIView

from forums.api.serializers import ThreadSerializer
from forums.models import Thread


class ThreadListCreateAPI(ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
