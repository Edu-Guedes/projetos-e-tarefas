from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    concluido = models.BooleanField(default=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return self.titulo