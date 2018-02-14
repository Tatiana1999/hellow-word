# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Enlaces

class AdminLinks(admin.ModelAdmin):
 	list_display =  ["url"]
admin.site.register(Enlaces,AdminLinks)

 