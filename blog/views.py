from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

from datetime import datetime

# Create your views here.

def current_date(request):
	"""View to return the current date."""

	return render(request, 'blog/current_date.html', {"date": datetime.now()})

def addition(request, nb1, nb2):
	"""View to perform the sum of 2 given integers."""

	total = nb1 + nb2
	return render(request, 'blog/addition.html', locals())
