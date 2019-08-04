from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics

from authentication import models
from . import serializers


class ListUsuario(generics.ListCreateAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer


class DetailUsuario(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer