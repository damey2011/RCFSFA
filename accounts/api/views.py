from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from accounts.api.permissions import IsOwnerOrReadOnly
from accounts.api.serializers import UserDetailSerializer, UserCreateSerializer, StudentProfileSerializer
from accounts.models import StudentProfile


class AccountListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        if self.request.method == 'GET':
            return UserDetailSerializer

    permission_classes = [AllowAny]  # Allow any to allow people to view other users and create new account even if
    # they are not reg

    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:  # Safe methods include get, options, head
    #         return [IsAuthenticated()]
    #     else:  # So this handles the post method
    #         return [AllowAny()]


class AccountRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class StudentProfileRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        try:
            return StudentProfile.objects.filter(user__username=self.kwargs['user__username'])
        except ObjectDoesNotExist:
            raise Http404

    lookup_field = 'user__username'
