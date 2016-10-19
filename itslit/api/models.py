from django.db import models
from django.contrib.auth.models import User


class Photos(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.image.name


class Offer(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ForeignKey(Photos, blank=True, null=True)
    green_text = models.CharField(max_length=255, blank=True, null=True)
    red_text = models.CharField(max_length=255, blank=True, null=True)
    price_before_discount = models.CharField(max_length=255, blank=True, null=True)
    price_after_discount = models.CharField(max_length=255, blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Biz(models.Model):
    name = models.CharField(max_length=255)
    offer = models.ManyToManyField(Offer)
    photos = models.ManyToManyField(Photos)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photos = models.ManyToManyField(Photos)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photos = models.ManyToManyField(Photos)
    hobbies = models.ManyToManyField(Hobby)

    def __str__(self):
        return self.name
