# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    re_path(r'ctr/(?P<key>.*)/', views.ctr, name='ctr'),
    re_path(r'mapping/.*', views.mapping, name='mapping'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
