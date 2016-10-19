from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Offer, Photos, Biz, Hobby, UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ('image',)


class OfferSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=False)

    class Meta:
        model = Offer
        fields = ('photo', 'name', 'green_text', 'red_text', 'price_before_discount', 'price_after_discount', 'likes')


class BizSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    offer = OfferSerializer(many=True)

    class Meta:
        model = Biz
        fields = ('photos', 'name', 'offer')


class HobbySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Hobby
        fields = ('photos', 'name', 'description')


class UserProfileSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    hobbies = HobbySerializer(many=True)
    user = UserSerializer(many=False)

    class Meta:
        model = User
        fields = ('photos', 'user', 'hobbies')