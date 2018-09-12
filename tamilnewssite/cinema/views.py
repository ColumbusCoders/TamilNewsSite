# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import feedparser
import sqlite3
#import rssReader as feed
import sys
sys.path.append("C:\\Sriram Sankar\\Python Projects\\TamilNewsSite\\tamilnewssite")
import common as config

# Create your views here.
#urls = config.cinema_urls
#print urls
feeds_ci =config.GetParseResults(config.cinema_urls)
feed_count = len(feeds_ci)
#print "total rows : "
#print feed_count
#conn = sqlite3.connect('test.db',check_same_thread=False)
#print "Opened database successfully";

#cursor = conn.execute("SELECT id, name, address, salary from CUSTOMER")
#results = cursor.fetchall()


#print "Operation done successfully";
#conn.close()

#print feeds_ci

context = {
        'cinema': feeds_ci,
        'rcount' : feed_count,
#        'cust': results
    }

def index(request):
    return render(request,'cinema/home.html',context)
