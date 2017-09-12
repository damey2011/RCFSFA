from django.conf.urls import url
from forums.api import views

urlpatterns = [
    url(r'^threads/$', views.ThreadListCreateAPI.as_view()),
    url(r'^threads/(?P<pk>\d+)$', views.ThreadRetrieveUpdateDelete.as_view(), name='thread-details'),
    url(r'^threads/comments/$', views.AllCommentListCreateAPI.as_view()),

    url(r'^threads/(?P<pk>\d+)/likes/$', views.ThreadLikesListCreateAPI.as_view(), name='thread-likes'),
    url(r'^threads/(?P<thread>\d+)/likes/(?P<pk>\d+)$', views.ThreadLikesDeleteAPI.as_view(), name='thread-likes-delete'),
    url(r'^threads/(?P<pk>\d+)/comments/$', views.ThreadCommentListCreateAPI.as_view(), name='thread-comments'),
    url(r'^threads/(?P<parent_id>\d+)/comments/(?P<pk>\d+)/$', views.CommentRetrieveUpdateDelete.as_view()),
    # parent id of thread here is also optional

    # The thread IDs here are not necessarily correct but just to maintain a uniform url pattern
    url(r'^comments/(?P<parent_id>\d+)/children/$', views.CommentChildrenListCreate.as_view(), name='comments-children'),
    url(r'^comments/(?P<parent_id>\d+)/children/(?P<pk>\d+)/$', views.CommentChildrenRetrieveUpdateDelete.as_view()),

    # Comment Children Children
    url(r'^comments/child/(?P<parent_id>\d+)/children/$', views.CommentChildrenChildrenListCreate.as_view(), name="children-children"),
    url(r'^comments/child/(?P<parent_id>\d+)/children/(?P<pk>\d+)/$', views.CommentChildrenChildrenRetrieveUpdateDelete.as_view()),
]
