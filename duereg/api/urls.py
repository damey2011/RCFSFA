from django.conf.urls import url

from programs.api import views

urlpatterns = [
    url(r'^$', views.ListCreateDueRecordView.as_view(), name='list-create-due-records'),
]
