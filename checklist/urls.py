from django.conf.urls import patterns, url

from checklist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cl/(\d+)/$', views.checklist),
)
