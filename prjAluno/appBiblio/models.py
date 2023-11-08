from django.db import models
from appAluno.models import Aluno
# Create your models here.


class Autor(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False)
   
    def __str__(self):
        return self.nome


class Livro (models.Model):
    codigo = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False)
    exemplares = models.IntegerField(default=0)
    autor = models.ForeignKey(Autor, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.titulo
    
    
class Estante(models.Model):
    numero = models.BigIntegerField(primary_key=True)
    livro = models.ForeignKey(Livro, on_delete=models.RESTRICT)
    quantidade = models.IntegerField()
    prateleira = models.IntegerField()
    
    
class FichaEmprestimo(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    livro = models.ForeignKey(Livro, on_delete=models.RESTRICT)
    aluno = models.ForeignKey(Aluno, on_delete=models.RESTRICT)
    retirada = models.DateField()
    devolucao = models.DateField(blank=True)
    