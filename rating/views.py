from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader
from .models import Movie, MovieRating
from django.contrib.auth.models import User
# Create your views here.

def index(request):
  latest_movie_list = Movie.objects.order_by('-release_date')
  context = {
    'latest_movie_list':latest_movie_list,
  }
  return render(request, 'rating/index.html', context)

def detail(request, movie_id):
  movie = get_object_or_404(Movie, pk = movie_id)
  return render(request, 'rating/detail.html', {'movie': movie})

def rate(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  try:
    rating_given = movie.rate_set.get(pk=request.POST['rating'])
  except(KeyError, MovieRating.DoesNotExist):
    return render(request, 'rating/detail.html', {
      'movie':movie,
      'error_message': "You didn't enter any rating.",
    })
  else:
    rating_given.save()
  return HttpResponseRedirect(reverse('rating:avgRating', args=(movie_id,)))
  #return render(request, 'rating/rate.html', movie_id, {'movie': movie})

def avgRating(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  return render(request, 'rating/avgRating.html', {'movie': movie})


def update_profile(request, user_id):
  user = User.objects.get(pk=user_id)
  user.save()