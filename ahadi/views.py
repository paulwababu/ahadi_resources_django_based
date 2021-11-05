from django.shortcuts import render, redirect
import requests
import time
import psutil
import os
from datetime import datetime
from .models import Monitor
from urllib.parse import urlparse
from django.core.paginator import Paginator

#traffic monitor
def traffic_monitor(request):
    dataSaved = Monitor.objects.all().order_by('-datetime')
    # Getting loadover15 minutes 
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = int((load15/os.cpu_count()) * 100)
    ram_usage = int(psutil.virtual_memory()[2])
    p = Paginator(dataSaved, 100)
    #shows number of items in page
    totalSiteVisits = (p.count)
    #find unique page viewers & Duration
    pageNum = request.GET.get('page', 1)
    page1 = p.page(pageNum)
    #unique page viewers
    a = Monitor.objects.order_by().values('ip').distinct()
    pp = Paginator(a, 10)
    #shows number of items in page
    unique = (pp.count)
    #update time
    now = datetime.now()
    data = {
        "now":now,
        "unique":unique,
        "totalSiteVisits":totalSiteVisits,
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "dataSaved": page1,
    }
    return render(request, 'traffic_monitor.html', data)

#home page
def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    response = requests.get('http://api.ipstack.com/'+ip+'?access_key=aabe5abccd63a6eee8eac2e9ebd3f8b1')
    rawData = response.json()
    continent = rawData['continent_name']
    country = rawData['country_name']
    capital = rawData['city']
    city = rawData['location']['capital']
    now = datetime.now()
    datetimenow = now.strftime("%Y-%m-%d %H:%M:%S")
    saveNow = Monitor(
        continent=continent,
        country=country,
        capital=capital,
        city=city,
        datetime=datetimenow,
        ip=ip
    )
    saveNow.save()
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def cvformatting(request):
    return render(request, 'cv-formatting.html')

def executivesearch(request):
    return render(request, 'executive-search.html')

def pricing(request):
    return render(request, 'pricing.html')

def projectbasedhiring(request):
    return render(request, 'project-based-hiring.html')

def rposervices(request):
    return render(request, 'rpo-services.html')

def traffic_monitor(request):
    return render(request, 'traffic_monitor.html')

def whatwedo(request):
    return render(request, 'what-we-do.html')

def whoweare(request):
    return render(request, 'who-we-are.html')