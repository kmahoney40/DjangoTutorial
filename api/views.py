from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer, TempSerializer, RunTimesSerializer
from .models import Bucketlist
#from ../water/models import Temp
from water.views import Temp, RunTimes

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

class CreateTempView(generics.ListCreateAPIView):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class CreateRunTimesView(generics.ListCreateAPIView):
    queryset = RunTimes.objects.all()
    serializer_class = RunTimesSerializer

    def perform_create(self, serializer):
        serializer.save()
