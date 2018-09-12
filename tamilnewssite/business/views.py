# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
import feedparser
import logging
import sys
sys.path.append("C:\Sriram Sankar\Python Projects\TamilNewsSite\tamilnewssite")
import common as config


# Create your views here.
feeds = config.GetParseResults(config.business_urls)

def index(request):
    return render(request,'business/home.html',{'test':feeds})
