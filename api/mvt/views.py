from rest_framework import generics
from .models import Dados
from .serializers import DadosSerializer
from datetime import datetime

class DadosListCreate(generics.ListCreateAPIView):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

    def perform_create(self, serializer):
        serializer.save(created_at=datetime.now())
