from cgitb import text
from random import choices
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.


class User(models.Model):
    USER_TYPE = (
    ('performer', 'performer'),
    ('studio', 'studio')
    )
    
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    types = models.CharField(
        max_length = 20,
        choices = USER_TYPE,
        default = 'performer') 
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='movies')

    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=1000)
    budget = models.IntegerField()

    def __str__(self):
        return self.name

class Role(models.Model):
    ROLE_CATEGORY = (
    ('lead', 'lead'),
    ('extra', 'extra'),
    ('secondary', 'secondary'),
    ('stunt', 'stunt')
    )

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='roles')

    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=1000)
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=100, blank=True)
    category = models.CharField(
        max_length = 40,
        choices = ROLE_CATEGORY,
        default = 'performer')

    def __str__(self):
        return self.name

class Actor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='actors')
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name='actors')
    
    name = models.CharField(max_length=100)
    videoFile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    image = models.ImageField()
    resume = models.FileField()

    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='votes')
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name='votes')

    def __str__(self):
        return str(self.actor)

class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)

    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message