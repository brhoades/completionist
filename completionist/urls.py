from django.conf.urls import patterns, include, url
from django.contrib import admin
from dh5bp.urls import urlpatterns as dh5bp_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'completionist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url( r'^admin/', include( admin.site.urls ) ),
    url( r'^cl/', include( 'checklist.urls', namespace='checklist' ) ),
    url( r'^', include( 'checklist.urls', namespace='checklist' ) ),
)

urlpatterns += dh5bp_urls
