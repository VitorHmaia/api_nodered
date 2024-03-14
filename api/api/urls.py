from django.urls import path
from myapp.views import DadosListCreate

urlpatterns = [
    path('api/dados/', DadosListCreate.as_view(), name='dados-list-create'),
]
