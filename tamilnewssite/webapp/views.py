# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import feedparser
import sys
sys.path.append("C:\\Sriram Sankar\\Python Projects\\TamilNewsSite\\tamilnewssite")
import common as config

# Create your views here.

feeds_bbc = config.GetParseResults(config.main_urls)
for i in feeds_bbc:
    print ("testing ---->")
    print (i.desc)

def index(request):
    return render(request,'webapp/tst.html',{'sports':feeds_bbc})
