from django.conf.urls import patterns, url, include

from checklist import views

urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")), #Auth handlers
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', views.profile, name="profile" ),
    url(r'^accounts/password_change_done/', 'django.contrib.auth.views.password_change_done', name="password_change_done"), #override for hardcoded ref in auth views
    url(r'^$', views.index, name='index'),
    url(r'^cl/(\d+)/$', views.checklist),
    url(r'^check/(\d+)/(\d+)/$', views.check),
    url(r'^newrun/(\d+)/$', views.newRun),
    url(r'^run/(\d+)/$', views.run),
)

