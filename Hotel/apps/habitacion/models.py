from django.db import models

# Create your models here.
class Habitacion(models.Model):
  numero=models.CharField(max_length=5)
  estado=models.CharField(max_length=10)
  costo= models.FloatField()
  descripcion=models.TextField()
  fkTipo= models.CharField(max_length=30)