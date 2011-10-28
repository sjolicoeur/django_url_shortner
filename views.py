# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from models import ShortUrl
from django.shortcuts  import get_object_or_404

# Create your views here.

def redirect_url(request, short_url) :
    short = get_object_or_404(ShortUrl, url_bit=short_url)
    return HttpResponseRedirect(short.url)