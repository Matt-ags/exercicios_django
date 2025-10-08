from django.db import models

# Create your models here.
class ESPECIALIDADE(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_especialidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField() 
    def __str__(self):
        return self.nome

class MEDICO(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=20)
    id_especialidade = models.ForeignKey(ESPECIALIDADE, on_delete=models.CASCADE)

