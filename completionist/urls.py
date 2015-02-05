from django.conf.urls import patterns, include, url
from django.contrib import admin
from dh5bp.urls import urlpatterns as dh5bp_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'completionist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url( r'^admin/', include( admin.site.urls ) ),
    url( r'^cl/', include( 'checklist.urls', namespace='checklist' ) ),
    url( r'^', include( 'checklist.urls', namespace='checklist' ) ),
)

urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += dh5bp_urls
