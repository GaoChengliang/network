# -*- coding:utf-8 -*-
from django.conf import settings
settings.configure() 
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import urllib
import re
from models import New

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'http://news.163.com/\d+.+?\.html'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        html = getHtml(imgurl)
        title = html[html.find('<title>'):html.find('<\\title>')]
        #New.objects.create(title=title, content=html)


html = getHtml("http://news.163.com/")

print getImg(html)
