from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	"""Basic view : Tell Welcome to the visitor."""

	welcome_msg = """<h1>Welcome to our blog!</h1>
	<p>The Breton pancakes are the best.<p/>
	"""
	return HttpResponse(welcome_msg) 
