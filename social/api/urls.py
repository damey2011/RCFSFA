from django.conf.urls import url

from social.api import views

urlpatterns = [
    url(r'^feeds/$', views.ListCreateFeed.as_view(), name='list-create-feed'),  # all feeds filtered based on user . Filter not yet implemented
    url(r'^feeds/user/(?P<user_username>\w+)/$', views.ListUserWrittenFeeds.as_view(), name='list-user-posts'),  # all feeds filtered based on user . Filter not yet implemented
    url(r'^feeds/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyFeed.as_view(), name='retrieve-update-destroy-feed'),  # all feeds filtered based on user . Filter not yet implemented
    url(r'^feeds/(?P<pk>\d+)/comments/$', views.ListCreateFeedComment.as_view(), name='list-create-feed-comment'),  # feed post comments
    url(r'^feeds/(?P<post>\d+)/comments/(?P<pk>\d+)/comments/$', views.ListCreateCommentComment.as_view(), name='list-create-comment-comment'),

    url(r'^feeds/(?P<pk>\d+)/likes/$', views.ListCreatePostLikes.as_view(), name='list-create-post-like'),  # feed like
    url(r'^feed-like/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPostLike.as_view(),
        name='retrieve-update-delete-post-like'),

    url(r'^message/(?P<user>\d+)/$', views.ListCreateMessage.as_view(), name='list-create-message'),

    url(r'^comments/(?P<pk>\d+)/$', views.RetrieveUpdateDeleteComment.as_view(), name='retrieve-update-delete-comment'),
    url(r'^comments/(?P<pk>\d+)/likes/$', views.ListCreateCommentLike.as_view(), name='list-create-comment-likes'),
    url(r'^comment-like/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyCommentLike.as_view(),
        name='retrieve-update-delete-comment-like'),

]
