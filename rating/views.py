from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, MovieRating
# Create your views here.

def index(request):
  return HttpResponse("This is the movie rating index Page.")

def detail(request, movie_id):
  return HttpResponse("You're looking at movie %s" % movie_id)

def rate(request, movie_id):
  return HttpResponse("You're rating movie %s" % movie_id)

def avgRating(request, movie_id):
  response = "You're looking at the average rating of movie %s"
  return HttpResponse(response % movie_id)
