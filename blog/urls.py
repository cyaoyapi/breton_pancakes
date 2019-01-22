from django.urls import path

from . import views

urlpatterns = [
	path('', views.home),
	path('article/<article_id>', views.view_article),
	path('articles/<str:tag>', views.view_articles_by_tag),
	path('articles/<int:year>/<int:month>', views.view_articles_by_month),
]
