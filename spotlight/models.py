from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.

USER_TYPE = (
    ('performer', 'performer'),
    ('studio', 'studio')
)

ROLE_CATEGORY = (
    ('lead', 'lead'),
    ('extra', 'extra'),
    ('secondary', 'secondary'),
    ('stunt', 'stunt')
)

class User(models.Model):
    type = USER_TYPE
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    coutnry = models.CharField(max_length=100)
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
    Movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='movies')

    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ethenicity = models.CharField(max_length=100, blank=True)
    category = ROLE_CATEGORY

    def __str__(self):
        return self.name

class Actor(models.Model):
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='actors')
    Role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name='actors')
    
    name = models.CharField(max_length=100)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    image = models.ImageField()
    resume = models.FileField()

    def __str__(self):
        return self.name

class Vote(models.Model):
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='votes')
    Actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name='votes')

    def __str__(self):
        return self

class Comment(models.Model):
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    Movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='comments', blank=True)
    Role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name='comments', blank=True)
    Actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name='comments', blank=True)

    message = models.CharField(max_length=200)

    def __str__(self):
        return self.text