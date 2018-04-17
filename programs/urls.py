from django.conf.urls import url

from programs import views

urlpatterns = [
    url(r'^$', view=views.AllProgramHome.as_view(), name='list-programs'),
    url(r'^create/$', view=views.ProgramCreate.as_view(), name='create-program'),
    url(r'^(?P<pk>\d+)/$', view=views.ProgramView.as_view(), name='view-program')
]