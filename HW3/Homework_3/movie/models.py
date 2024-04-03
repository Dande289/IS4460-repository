from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    rating = models.IntegerField(default=0)
    genre = models.CharField(max_length=25, blank=True, null=True)


class User(models.Model):
    username = models.CharField(max_length = 50, default = "")
    password = models.CharField(max_length = 255, default = "")
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)