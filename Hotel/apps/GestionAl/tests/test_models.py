from django.test import TestCase
from apps.GestionAl.models import Alquiler, Registrador, Estado

class AlquilerTestCase(TestCase):
    def setUp(self):
        Alquiler.objects.create(fechaHoraEntrada="2020-10-25", fechaHoraSalida="2020-10-27", costoTotal=200000, observacion="grande con vista al mar")
        Alquiler.objects.create(fechaHoraEntrada="2021-12-24", fechaHoraSalida="2021-12-26", costoTotal=300000, observacion="pequeño con dos camas")
    def  test_alquileres_tienen_fechas(self):
        """los alquileres tienen una fecha de entrada y salida"""
        fecha1=Alquiler.objects.get(fechaHoraSalida="2020-10-27")
        fecha2=Alquiler.objects.get(fechaHoraSalida="2021-12-26")
        self.assertEqual(fecha1.fechaHoraSalida, fecha2.fechaHoraSalida, "2020-10-27" )
        self.assertEqual(fecha2.fechaHoraSalida, fecha1.fechaHoraSalida, "2021-12-26" )
