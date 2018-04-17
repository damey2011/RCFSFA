from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views

from accounts import views

urlpatterns = [
    url(r'^signup/$', view=views.SignUpView.as_view(), name='signup'),
    url(r'^signin/$', view=views.SignInView.as_view(), name='signin'),
    url(r'^users/$', view=views.ListUsers.as_view(), name='list-users'),
    url(r'^users/create/$', view=views.AdminCreateUser.as_view(), name='create-user'),
    url(r'^users/edit/(?P<pk>\d+)/$', view=views.AdminEditUser.as_view(), name='edit-user'),
    url(r'^users/delete/(?P<pk>\d+)/$', view=views.AdminDeleteUser.as_view(), name='delete-user'),
    url(r'^users/create/success/$', view=views.UserCreateSuccess.as_view(), name='user-create-success'),
    url(r'^users/edit/success/$', view=views.UserEditSuccess.as_view(), name='user-edit-success'),
    url(r'^users/delete/success/$', view=views.UserDeleteSuccess.as_view(), name='user-delete-success'),
]
