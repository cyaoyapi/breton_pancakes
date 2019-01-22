from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	"""Basic view : Tell Welcome to the visitor."""

	welcome_msg = """<h1>Welcome to our blog!</h1>
	<p>The Breton pancakes are the best.<p/>
	"""
	return HttpResponse(welcome_msg) 

def view_article(request, article_id):
	"""Basic view to display an article."""

	return HttpResponse(f"You want to get article N° {article_id}") 