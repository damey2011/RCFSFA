from django.conf.urls import url

from accounts.api import views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^$', views.AccountListCreateAPIView.as_view()),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^might-know/$', views.MightKnowUsers.as_view()),
    url(r'^(?P<username>[\w-]+)/$', views.AccountRetrieveUpdateDelete.as_view()),
    url(r'^(?P<username>[\w-]+)/follow/$', views.CreateUserFollowing.as_view()),
    url(r'^(?P<username>[\w-]+)/unfollow/$', views.DeleteUserFollowing.as_view()),
    url(r'^(?P<user__username>[\w-]+)/profile/$', views.UserProfileRetrieveUpdateDelete.as_view()),
]
