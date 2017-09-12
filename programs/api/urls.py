from django.conf.urls import url

from programs.api import views

urlpatterns = [
    url(r'^$', views.ListCreateProgram.as_view(), name='list-create-program'),
    url(r'^(?P<pk>\d+)$', views.RetrieveUpdateDestroyProgram.as_view(), name='retrieve-update-delete')
]