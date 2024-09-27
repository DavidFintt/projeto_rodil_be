from .models import Mensagem
from rest_framework import serializers


class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = "__all__"
        extra_kwargs = {"lida": {"read_only": True}, "data": {"read_only": True}}
