from django.urls import path, re_path

from . import views

urlpatterns = [
	path('current_date/', views.current_date, name='current_date'),
	path('addition/<int:nb1>/<int:nb2>', views.addition, name='addition'),
]
