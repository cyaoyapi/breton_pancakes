from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.home),
	path('article/<article_id>', views.view_article),
	path('articles/<str:tag>', views.view_articles_by_tag),
	re_path('^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.view_articles_by_month),
]
