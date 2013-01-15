from __future__ import absolute_import
from django.conf.urls import patterns, url
from gubbins.app import ReusableAppURLs
from passwords.views import PasswordGenerationView


urlpatterns = patterns('',
    url('^$',
        PasswordGenerationView.as_view(),
        name='generate'),

)

urls = ReusableAppURLs('passwords', urlpatterns)