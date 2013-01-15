from django.conf.urls import patterns, include, url
import core.urls, account.urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include(account.urls.urls())),
    url(r'', include(core.urls.urls())),
    url(r'^account/', include('social_auth.urls')),
)

from django.conf import settings
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )