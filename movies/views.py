from django.shortcuts import render
from rest_framework import viewsets
from .models import Moviedata
from .serializers import MovieSerializer

# Create your views here.
class MovieviewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionviewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyviewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MovieSerializer
