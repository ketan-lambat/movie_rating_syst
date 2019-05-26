from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views



app_name = 'rating'
urlpatterns = [
  path('user/login/home', views.index, name='index'),
  path('user/login/<int:movie_id>/', views.detail, name='detail'),
  path('user/login/<int:movie_id>/rate/', views.rate, name='rate'),
  path('user/login/<int:movie_id>/avgRating/', views.avgRating, name='avgRating'),

]