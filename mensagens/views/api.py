from rest_framework import status
from rest_framework.response import Response
from ..serializers import MensagemSerializer
from ..models import Mensagem
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
@permission_classes([AllowAny])
def insert_mensagem(request):
    try:
        serializer = MensagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def return_mensagens(request):
    try:
        mensagens = Mensagem.objects.all()
        serializer = MensagemSerializer(mensagens, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH'])
@permission_classes([AllowAny])
def ler_mensagem(request):
    try:
        mensagem = Mensagem.objects.get(pk=request.data['mensagem_id'])
        mensagem.lida = True
        mensagem.save()
        return Response({"mensagem": "Mensagem lida"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_mensagem(request):
    try:
        mensagem = Mensagem.objects.get(pk=request.data['mensagem_id'])
        mensagem.delete()
        return Response({"mensagem": "Mensagem deletada"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)