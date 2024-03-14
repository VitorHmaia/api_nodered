from django.urls import path
from mvt.views import DadosListCreate
from django.views.generic import TemplateView

urlpatterns = [
    path('api/dados/', DadosListCreate.as_view(), name='dados-list-create'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
