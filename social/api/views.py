# Create your views here.
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from social.api.serializers import FeedPostSerializer, PostLikeSerializer, CommentLikeSerializer, \
    PostCommentSerializer, CommentCommentSerializer
from social.models import FeedPost, Comment, PostLike, CommentLike


class ListCreateFeed(ListCreateAPIView):
    queryset = FeedPost.objects.all()
    serializer_class = FeedPostSerializer


class ListUserWrittenFeeds(ListAPIView):
    queryset = FeedPost.objects.all()
    serializer_class = FeedPostSerializer
    lookup_field = 'user_username'


class RetrieveUpdateDestroyFeed(RetrieveUpdateDestroyAPIView):
    queryset = FeedPost.objects.all()
    serializer_class = FeedPostSerializer


class ListCreateFeedComment(ListCreateAPIView):
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'], parent=None)

    serializer_class = PostCommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        post = self.kwargs.get('pk', None)
        if post is not None:
            serializer.save(post_id=post, user=user)
        else:
            raise JsonResponse("No Parent Post", status=500)


class ListCreateCommentComment(ListCreateAPIView):
    serializer_class = CommentCommentSerializer

    def get_queryset(self):
        parent = self.kwargs.get('pk', None)
        return Comment.objects.filter(parent_id=parent)

    def perform_create(self, serializer):
        user = self.request.user
        parent = self.kwargs.get('pk', None)
        post = self.kwargs.get('post', None)

        if parent is not None and post is not None:
            serializer.save(post_id=post, parent_id=parent, user=user)
        else:
            raise JsonResponse("No Parent Post", status=400)


class RetrieveUpdateDeleteComment(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCommentSerializer


class ListCreateMessage(ListCreateAPIView):
    queryset = FeedPost.objects.all()
    serializer_class = FeedPostSerializer


class ListCreatePostLikes(ListCreateAPIView):
    def get_queryset(self):
        return PostLike.objects.filter(post_id=self.kwargs['pk'])

    serializer_class = PostLikeSerializer

    # def perform_create(self, serializer):
    #     if


class ListCreateCommentLike(ListCreateAPIView):
    def get_queryset(self):
        return CommentLike.objects.filter(comment_id=self.kwargs['pk'])

    serializer_class = CommentLikeSerializer


class RetrieveUpdateDestroyPostLike(RetrieveUpdateDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer


class RetrieveUpdateDestroyCommentLike(RetrieveUpdateDestroyAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
