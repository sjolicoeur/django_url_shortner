# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<short_url>.*)/?$', 'views.redirect_url', {}, 'shortner_url' )
)