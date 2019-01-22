from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('article/<int:article_id>', views.view_article, name='article'),
	path('articles/tag/<str:tag>', views.view_articles_by_tag, name='articles_tag'),
	re_path('^articles/(?P<year>\d{4})/(?P<month>\d{1,2})', views.view_articles_by_month, name='articles_year_month'),
	path('article/redirect/<int:article_id>', views.article_redirect, name='article_redirect'),
]
