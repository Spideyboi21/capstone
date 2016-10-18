from django.db import models
from django.contrib.auth.models import User

class Photos(models.Model):
    image = models.ImageField()

class Offer(models.Model):
    name = models.CharField(max_length = 255)
    photos = models.ManyToManyField(Photos, blank = True, null = True)

    def __str__(self):
        return self.name

class Biz(models.Model):
    name = models.CharField(max_length = 255)
    offer = models.ManyToManyField(Offer, blank = True, null = True)
    photos = models.ManyToManyField(Photos, blank = True, null = True)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    photos = models.ManyToManyField(Photos, blank = True, null = True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photos = models.ManyToManyField(Photos, blank = True, null = True)
    hobbies = models.ManyToManyField(Hobby, blank = True, null = True)

    def __str__(self):
        return self.name
