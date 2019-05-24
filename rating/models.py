from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Movie(models.Model):
  movieTitle = models.CharField(max_length=200, unique=True)
  #def get_avg_rating(self):

  def __str__(self):
    return self.movieTitle


class MovieRating(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  movieRating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
  def __str__(self):
    return self.movieRating
