from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from forums.api.pagination import LikePagination
from forums.api.serializers import ThreadSerializer, CommentSerializer, ChildCommentSerializer, LikeSerializer
from forums.models import Thread, Comment, ChildComment, Like


class ThreadListCreateAPI(ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class ThreadRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    lookup_field = 'pk'


class AllCommentListCreateAPI(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ThreadCommentListCreateAPI(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent_id=self.kwargs['pk'])


class CommentRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


class CommentChildrenListCreate(ListCreateAPIView):
    serializer_class = ChildCommentSerializer

    def get_queryset(self):
        return ChildComment.objects.filter(parent=self.kwargs['parent_id'], parent_type=1)


class CommentChildrenRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ChildCommentSerializer

    def get_queryset(self):
        return ChildComment.objects.filter(parent=self.kwargs['parent_id'], parent_type=1)

    lookup_field = 'pk'


class CommentChildrenChildrenListCreate(ListCreateAPIView):
    serializer_class = ChildCommentSerializer

    def get_queryset(self):
        return ChildComment.objects.filter(parent=self.kwargs['parent_id'], parent_type=2)


class CommentChildrenChildrenRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ChildCommentSerializer

    def get_queryset(self):
        return ChildComment.objects.filter(parent=self.kwargs['parent_id'], parent_type=2)

    lookup_field = 'pk'


class ThreadLikesListCreateAPI(ListCreateAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        try:
            return Like.objects.filter(type=0, parent=self.kwargs['pk']).order_by('-timestamp')
        except ObjectDoesNotExist:
            raise Http404

    pagination_class = LikePagination


class ThreadLikesDeleteAPI(DestroyAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    lookup_field = 'pk'
