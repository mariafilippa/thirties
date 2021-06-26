# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from .data import notebook
from .models import UserMapping

@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def mapping(request):
    mappings = UserMapping.objects.all()
    paginator = Paginator(mappings, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {}
    context['segment'] = 'mapping'
    context['page_obj'] = page_obj
    context['chart'] = {
        "element": 'morris-line-smooth-chart',
        "data": notebook.LABELED_MONTH_COUNT,
        "xkey": 'count',
        "redraw": True,
        "resize": True,
        "ykeys": ['new', 'adv'],
        "hideHover": 'auto',
        "responsive": True,
        "labels": ['新手', '進階'],
        "lineColors": ['#1de9b6', '#A389D4'],
        "pointSize": 0,
        "lineWidth": 0,
        "fillOpacity": 0.5,
        "behaveLikeLine": True,
        "gridLineColor": '#d2d2d2',
        "parseTime": False
    }
    context['chart2'] = {
        "element": 'morris-line-smooth-chart-2',
        "data": notebook.LABELED_MONTH_DURATION,
        "xkey": 'duration',
        "redraw": True,
        "resize": True,
        "ykeys": ['new', 'adv'],
        "hideHover": 'auto',
        "responsive": True,
        "labels": ['新手', '進階'],
        "lineColors": ['#1de9b6', '#A389D4'],
        "pointSize": 0,
        "lineWidth": 0,
        "fillOpacity": 0.5,
        "behaveLikeLine": True,
        "gridLineColor": '#d2d2d2',
        "parseTime": False
    }

    html_template = loader.get_template( 'mapping.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def ctr(request, key):

    context = {}
    context['chart'] = {
        "element": 'morris-line-smooth-chart',
        "data": notebook.CTR,
        "xkey": 'date',
        "redraw": True,
        "resize": True,
        "ykeys": ['ctr'],
        "hideHover": 'auto',
        "responsive":True,
        "labels": ['CTR'],
        "lineColors": ['#1de9b6']
    }

    html_template = loader.get_template( 'ctr.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
