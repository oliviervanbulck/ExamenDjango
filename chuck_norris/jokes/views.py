from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
import urllib, urllib2
import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def index(request):
	return render(request, 'jokes/index.html', {})
    #return render(request, 'jokes/index.html')

def joke(request, first_name, last_name):
	url = 'http://api.icndb.com/jokes/random?firstName=' + urllib.quote(first_name) + '&lastName=' + urllib.quote(last_name)
	response = urllib2.urlopen(url)
	data = json.load(response)
	
	if r.exists('joke:' + str(data['value']['id'])) == 0:
		r.set('joke:' + str(data['value']['id']), data['value']['joke'])
	
	return render(request, 'jokes/index.html', {'joke': data['value']['joke'], 'first_name': first_name, 'last_name': last_name})