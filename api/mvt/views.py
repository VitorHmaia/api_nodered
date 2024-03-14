from django.shortcuts import render

from rest_framework import generics
from .models import Dados
from .serializers import DadosSerializer

class DadosListCreate(generics.ListCreateAPIView):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer
