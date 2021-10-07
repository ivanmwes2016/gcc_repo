from django.shortcuts import render
from rest_framework import generics
from .serializer import EventSerializer
from .models import  Event

class EventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
     
      