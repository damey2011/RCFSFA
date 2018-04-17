from rest_framework import filters, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from programs.api.pagination import ProgrammeInterestedAttendeePagination
from programs.api.serializers import ProgrammeSerializer, ProgrammeInterestedAttendeeSerializer
from programs.models import Programme, ProgramInterestedAttendees


class ListCreateProgram(ListCreateAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAuthenticatedOrReadOnly]


class RetrieveUpdateDestroyProgram(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgrammeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Programme.objects.get(pk=self.kwargs['pk'])


class ListCreateProgrammeInterest(ListCreateAPIView):
    def get_queryset(self):
        return ProgramInterestedAttendees.objects.filter(programme_id=self.kwargs['pk'])
    serializer_class = ProgrammeInterestedAttendeeSerializer
    pagination_class = ProgrammeInterestedAttendeePagination


class ListCreateDueRecordView(ListCreateAPIView):
    pass