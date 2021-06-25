# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import UserMapping


@admin.register(UserMapping)
class UserMappingAdmin(admin.ModelAdmin):
    pass
