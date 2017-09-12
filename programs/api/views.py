from rest_framework import filters, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from programs.api.serializers import ProgrammeSerializer
from programs.models import Programme


class ListCreateProgram(ListCreateAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer()
    filter_backends = (filters.SearchFilter,)
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class RetrieveUpdateDestroyProgram(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgrammeSerializer()
    permission_classes = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        return Programme.objects.get(pk=self.kwargs['pk'])
