from django.shortcuts import render
import simplejson as json
from django.template import loader

# Create your views here.
from django.http import HttpResponse
import requests
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""
def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))



def get_city(request):
    name = request.GET['city']
    req = requests.get('https://www.metaweather.com/api/location/search/?query=' + str(name), params=request.GET)
    template = loader.get_template('app/index.html')
    context = {
        'cities':req.json(),
    }
    return HttpResponse(template.render(context, request))
    

def get_weather(request):
    woeid = request.GET['woeid']
    req = requests.get('https://www.metaweather.com/api/location/' + str(woeid) + '/', params=request.GET)
    if req.status_code == 200:
        weather = req.json()
        template = loader.get_template('app/index.html')
        context = {
            'weather':weather['consolidated_weather'],
            'cities': [{'title': weather['title']}]
        }
    return HttpResponse(template.render(context, request))
