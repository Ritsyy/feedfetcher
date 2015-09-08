from django.conf import settings
from BeautifulSoup import BeautifulSoup
from .feeds import *
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from .forms import FeedUrlForm
from .models import *

# Create your views here.

def home(request):
	form = FeedUrlForm(request.POST or None)
	url = ""
	obj = feedUrl.objects.all()
	if form.is_valid():
		save_it = form.save(commit = False)
		url= save_it.url
		save_it.save()
		form = FeedUrlForm()
		obj = feedUrl.objects.all()
		return render_to_response("index.html", locals(), context_instance = RequestContext(request))

	return render_to_response("index.html", locals(), context_instance = RequestContext(request))

def result(request, url_id):
	value = {}
	print url_id
	obj = feedUrl.objects.get(pk=url_id)
	url = obj.url
	value = feeddata(url)
	for i in value:
		i["description"] = BeautifulSoup(i["description"]).text
	return render_to_response("result.html", {'value':value}, context_instance = RequestContext(request))	