# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ClientProfile, YoungProfile

# Register your models here.
admin.site.register(YoungProfile)
admin.site.register(ClientProfile)
