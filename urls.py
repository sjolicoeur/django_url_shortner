# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from views import redirect_url

urlpatterns = patterns('',
    (r'^(?P<short_url>.*)/?$', redirect_url, {}, 'shortner_url' )
)