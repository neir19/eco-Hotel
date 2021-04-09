from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    id_Nacionalidad=models.IntegerField(primary_key=True)
    pais=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nacionalidad)

class Cliente(models.Model):
  id_Cliente=models.IntegerField(primary_key=True)
  nombre=models.CharField(max_length=50)
  apellido=models.CharField(max_length=50)
  direccion=models.TextField()
  documento=models.CharField(max_length=30)
  telefono=models.CharField(max_length=12)
  nacionalidad=models.ForeignKey(Nacionalidad,null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
        return '{}'.format(self.nombre)
