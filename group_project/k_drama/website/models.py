from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.PositiveIntegerField()
    rating = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=255, default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)


class Review(models.Model):
    text = models.TextField()
    rating = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Review for {self.show.title} by {self.user.username}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


