from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer, PhotoSerializer, OfferSerializer
from api.serializers import BizSerializer, HobbySerializer, UserProfileSerializer
from .models import Offer, Biz, Hobby, UserProfile


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Create your views here.
class OfferViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def list(self, request):
        queryset = Offer.objects.all()
        serializer = OfferSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Offer.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = OfferSerializer(item)
        return Response(serializer.data)


class BizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Biz.objects.all()
    serializer_class = BizSerializer


class HobbyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
