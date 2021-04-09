from django import forms
from apps.GestionAl.models import Alquiler

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

    