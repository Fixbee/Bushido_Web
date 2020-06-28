from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('achievements/', views.achievements, name='achievements'),
	path('forms/', views.forms, name='forms'),
	path('events/', views.events, name='events'),
	path('instructors/', views.instructors, name='instructors'),
	path('gallery/', views.gallery, name='gallery'),
	path('registration/', views.registration, name='registration'),
]
