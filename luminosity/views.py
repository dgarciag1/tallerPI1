from django.shortcuts import render
from rest_framework import viewsets
from .models import Luminosity
from .serializers import LuminositySerializer
# Create your views here.


class LuminosityViewSet(viewsets.ModelViewSet):
    queryset = Luminosity.objects.all().order_by('-created')
    serializer_class = LuminositySerializer
