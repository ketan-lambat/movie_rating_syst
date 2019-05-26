from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Movie(models.Model):
  movieTitle = models.CharField(max_length=200, unique=True)
  release_date = models.DateField('date released')
  def get_avg_rating(self):
    avg = MovieRating.objects.aggregate(Avg('movieRating'))
    return avg
  def __str__(self):
    return self.movieTitle


class MovieRating(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  movieRating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
  def __str__(self):
    return self.movieRating


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()