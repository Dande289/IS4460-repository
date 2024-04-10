from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.PositiveIntegerField()
    rating = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='show_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    birth_place = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    movies = models.ManyToManyField(Show, related_name='actors')
    image = models.ImageField(upload_to='actor_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Character(models.Model):
    character_name = models.CharField(max_length=255)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='actor', null=True, blank=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='actor', null=True, blank=True)
    
class Award(models.Model):
    award_name = models.CharField(max_length=50, default="")
    description = models.TextField()
    award_year = models.PositiveIntegerField()
    category = models.CharField(max_length=255, default="")
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='awards', null=True, blank=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='awards', null=True, blank=True)
    
    def __str__(self):
        return self.award_name
