from django.db import models

# Create your models here.

class TipoHabitacion(models.Model):
  nombre= models.CharField(max_length=20)
  descripcion=models.TextField()

  def __str__(self):
    return '{}'.format(self.nombre)



class Habitacion(models.Model):
  numero=models.CharField(max_length=5)
  estado=models.CharField(max_length=10)
  costo= models.FloatField()
  descripcion=models.TextField()
  fkTipo= models.ForeignKey(TipoHabitacion,null=True, blank=True, on_delete=models.CASCADE) 

  