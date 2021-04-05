from django import forms
from apps.habitacion.models import Habitacion,TipoHabitacion

class ThabitacionForm(forms.ModelForm):
  class Meta:
    model = TipoHabitacion

    fields =[
      'nombre',
      'descripcion',
    ]
    labels={
      'nombre': 'tipo de habitacion',
      'descripcion': 'descripcion'
    }
    widget={
      'nombre':           forms.TextInput(attrs={'class': 'form-control'}),
      'description':      forms.TextInput(attrs={'class': 'form-control'}),
    }

class HabitacionForm(forms.ModelForm):
  class Meta:
    model=Habitacion

    fields =[
      'numero',
      'estado',
      'costo',
      'descripcion',
      'fkTipo',
    ]
    labels={
      'numero': 'nomenclatura',
      'estado': 'estado',
      'costo': 'costo',
      'descripcion':'descripcion',
      'fkTipo':'tipo',
    }
    widget={
      'numero':      forms.TextInput(attrs={'class': 'form-control'}),
      'estado':      forms.TextInput(attrs={'class': 'form-control'}),
      'costo':       forms.TextInput(attrs={'class': 'form-control'}),
      'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
      'fkTipo':      forms.TextInput(attrs={'class': 'form-control'}),
    }


