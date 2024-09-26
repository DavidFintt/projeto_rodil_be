from django.db import models

# Create your models here.

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    pergunta = models.TextField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return self.mensagem
    
    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        db_table = 'mensagem'