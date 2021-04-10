from django import forms
from apps.GestionAl.models import Alquiler, Registrador

class AlquilerForm(forms.ModelForm):
  class Meta:
    model=Alquiler

    fields = [

            'fechaHoraEntrada',
            'fechaHoraSalida',
            'costoTotal',
            'observacion',
            'registrador',
            'estado',
        ]
    labels = {
            'fechaHoraEntrada': 'fechaHoraEntrada',
            'fechaHoraSalida': 'fechaHoraSalida',
            'costoTotal': 'costoTotal',
            'observacion': 'observacion',
            'registrador': 'registrador',
            'estado': 'estado',
        }
    widgets = {
            'fechaHoraEntrada': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaHoraSalida': forms.TextInput(attrs={'class': 'form-control'}),
            'costoTotal': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
            'registrador': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistradorForm(forms.ModelForm):
  class Meta:
    model=Registrador

    fields = [

            'nombre',
            'direccion',
            'documento',
            'telefono',
            'estado',
            'observacion',

    ]

    labels = {
            'nombre': 'nombre',
            'direccion': 'direccion',
            'documento': 'documento',
            'telefono': 'telefono',
            'estado': 'estado',
            'observacion': 'observacion',
        }
    widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

    