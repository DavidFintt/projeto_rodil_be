from .models import Mensagem
from rest_framework import serializers


class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        exclude = ['data', 'lida']