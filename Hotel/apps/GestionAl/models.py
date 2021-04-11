from django.db import models

# Create your models here.

class Estado(models.Model):
    Nombre=models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.Nombre)

class Registrador(models.Model):
    nombre=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    documento=models.IntegerField()
    telefono=models.IntegerField()
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE)
    observacion=models.CharField(max_length=90)

    def __str__(self):
        return '{}'.format(self.nombre)

class Alquiler(models.Model):
    
    fechaHoraEntrada=models.DateField()
    fechaHoraSalida=models.DateField()
    costoTotal=models.IntegerField()
    observacion=models.CharField(max_length=60)
    registrador=models.ForeignKey(Registrador, on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.costoTotal)


