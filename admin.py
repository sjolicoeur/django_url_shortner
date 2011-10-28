# -*- coding: utf-8 -*-
from django.contrib import admin
from models import ShortUrl

class ShortUrlAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('url_bit','url')

#####
admin.site.register(ShortUrl, ShortUrlAdmin)
