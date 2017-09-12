from django.conf.urls import url

from campus.api import views

urlpatterns = [
    url(r'^schools/$', views.SchoolListCreateAPI.as_view()),
    url(r'^schools/(?P<pk>\d+)$', views.SchoolRetrieveUpdateDelete.as_view(), name='school-details'),
]