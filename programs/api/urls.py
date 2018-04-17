from django.conf.urls import url

from programs.api import views

urlpatterns = [
    url(r'^$', views.ListCreateProgram.as_view(), name='list-create-program'),
    url(r'^(?P<pk>\d+)/$', views.RetrieveUpdateDestroyProgram.as_view(), name='retrieve-update-delete'),
    url(r'^(?P<pk>\d+)/interest/$', views.RetrieveUpdateDestroyProgram.as_view(), name='programme-interest'),
    url(r'^(?P<pk>\d+)/accommodation/$', views.RetrieveUpdateDestroyProgram.as_view(),
        name='list-create-programme-accommodation'),
    url(r'^(?P<pk>\d+)/accommodation/book/$', views.RetrieveUpdateDestroyProgram.as_view(), name='book-accommodation'),
]
