from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=500,null=True)
    director = models.CharField(max_length=100,null=True)
    release_year = models.CharField(max_length=50,null=True)
    budget = models.CharField(max_length=50,null=True)
    runtime = models.CharField(max_length=50,null=True)
    rating = models.CharField(max_length=50,null=True)
    genre = models.CharField(max_length=50,null=True)
    test_class = models.CharField(max_length=50,null=True)
class User(models.Model):
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=255,null=False)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=100,null=True)

class Role(models.Model):
    username = models.CharField(max_length=50,null=False)
    role = models.CharField(max_length=20,null=False)
