from django.conf import settings
from BeautifulSoup import BeautifulSoup
from .feeds import *
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from .forms import FeedUrlForm

# Create your views here.

def home(request):
	form = FeedUrlForm(request.POST or None)
	value = {}
	url = ""
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		url= save_it.url
		value = feeddata(url)
		for i in value:
			i["description"] = BeautifulSoup(i["description"]).text
		return render_to_response("result.html", {'value': value}, context_instance = RequestContext(request))
	return render_to_response("index.html", locals(), context_instance = RequestContext(request))

	# return render_to_response("index.html", locals(),
	# context_instance = RequestContext(request))