from .views.api import insert_mensagem, return_mensagens, delete_mensagem, ler_mensagem
from django.urls import path

urlpatterns = [
    path('api/mensagens/insert/', insert_mensagem),
    path('api/mensagens/load/', return_mensagens),
    path('api/mensagens/delete/', delete_mensagem),
    path('api/mensagens/ler/', ler_mensagem),
]