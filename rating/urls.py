from django.urls import path
from . import views

app_name = 'rating'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:movie_id>/', views.detail, name='detail'),
  path('<int:movie_id>/rate/', views.rate, name='rate'),
  path('<int:movie_id>/avgRating/', views.avgRating, name='avgRating'),

]