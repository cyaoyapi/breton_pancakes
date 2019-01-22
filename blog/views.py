from django.http import HttpResponse, Http404
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

	if article_id > 100:
		raise Http404
	return HttpResponse(f"You want to get article N° <strong>{article_id}</strong>") 

def view_articles_by_tag(request, tag):
	"""Basic view to display a list of articles by given tag."""

	return HttpResponse(f"You want the list of articles with tag : <strong>{tag}</strong>") 

def view_articles_by_month(request, year, month):
	"""Basic view to display a list of articles by given year and month."""

	return HttpResponse(f"You want the list of articles of : <strong>{month}/{year}</strong>") 

