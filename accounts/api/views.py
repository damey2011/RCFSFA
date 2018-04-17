from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from accounts.api.permissions import IsOwnerOrReadOnly
from accounts.api.serializers import UserDetailSerializer, UserCreateSerializer, MemberProfileSerializer, \
    CoordinatorProfileSerializer, ExcoProfileSerializer, CreateUserFollowingSerializer, MightKnowSerializer
from accounts.models import MemberProfile, UserRole, CoordinatorProfile, ExcoProfile, UserFollowing


class AccountListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        if self.request.method == 'GET':
            return UserDetailSerializer

    permission_classes = [
        AllowAny]  # Allow any to allow people to view other manage_users and create new account even if

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
    permission_classes = [IsOwnerOrReadOnly]


class UserProfileRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        user_role = UserRole.objects.get_or_create(user=self.request.user)[0].role
        if user_role == 0:
            return MemberProfileSerializer
        elif user_role == 1:
            return CoordinatorProfileSerializer
        elif user_role == 2:
            return ExcoProfileSerializer

    def get_queryset(self):
        user_role = UserRole.objects.get_or_create(user=self.request.user)[0].role
        if user_role == 0:
            try:
                return MemberProfile.objects.filter(user__username=self.kwargs['user__username'])
            except ObjectDoesNotExist:
                raise Http404
        elif user_role == 1:
            try:
                return CoordinatorProfile.objects.filter(user__username=self.kwargs['user__username'])
            except ObjectDoesNotExist:
                raise Http404
        elif user_role == 2:
            try:
                return ExcoProfile.objects.filter(user__username=self.kwargs['user__username'])
            except ObjectDoesNotExist:
                raise Http404

    lookup_field = 'user__username'


class MightKnowUsers(ListAPIView):
    def get_queryset(self):
        return User.objects.all().exclude(pk__in=UserFollowing.objects.filter(user=self.request.user).values('id'))\
            .exclude(pk=self.request.user.id)[:4]

    serializer_class = MightKnowSerializer
    permission_classes = [IsAuthenticated]


class CreateUserFollowing(CreateAPIView):
    serializer_class = CreateUserFollowingSerializer
    queryset = UserFollowing.objects.all()

    def create(self, request, *args, **kwargs):
        user = self.request.user
        follows = User.objects.get(username=self.kwargs['username'])

        return Response(CreateUserFollowingSerializer(UserFollowing.objects.create(user=user, follows=follows)).data, status=201)


class DeleteUserFollowing(CreateAPIView):
    serializer_class = CreateUserFollowingSerializer
    queryset = UserFollowing.objects.all()

    def create(self, request, *args, **kwargs):
        user = self.request.user
        follows = User.objects.get(username=self.kwargs['username'])

        UserFollowing.objects.filter(user=user, follows=follows).delete()

        return Response({'status': True}, status=201)
