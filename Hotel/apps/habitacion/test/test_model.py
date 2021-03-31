from django.test import TestCase
from apps.habitacion.models import Habitacion

class HabitacionTestCase(TestCase):
  def setUp(self):
    Habitacion.objects.create(numero="A01",estado="disponible",costo="80000",descripcion="primer piso, con baño",fkTipo="sencilla")
    Habitacion.objects.create(numero="A02",estado="ocupado",costo="80000",descripcion="primer piso, con baño",fkTipo="sencilla")

  def test_habitacion_estado(self):
    """sólo puede haber un estado"""
    A01=Habitacion.objects.get(estado="ocupado")
    A02=Habitacion.objects.get(estado="disponible")

    self.assertEqual(A01.estado,A02.estado,"disponible")
    self.assertEqual(A02.estado,A01.estado,"ocupado")