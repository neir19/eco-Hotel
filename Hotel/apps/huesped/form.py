from django import forms
from .models import Cliente

class GestionForm(forms.ModelForm):
  class Meta:
    model= Cliente
    fields= [
      'id_Cliente',
      'nombre',
      'apellido',
      'direccion',
      'documento',
      'telefono',
      'nacionalidad'
    ]

    labels= {
      'id_Cliente': 'Id huesped',
      'nombre': 'Nombre',
      'apellido': 'Apellido',
      'direccion':'Dirección',
      'documento': 'Documento',
      'telefono': 'Telefono',
      'nacionalidad': 'Nacionalidad'
    }

    widgets= {
      'id_Cliente': forms.TextInput (attrs= {'class' : "form-group col-md-3"}),
      'nombre': forms.TextInput (attrs= {'class' : "form-group col-md-3"}),
      'apellido': forms.TextInput (attrs= {'class' : "form-group col-md-3"}),
      'direccion': forms.TextInput (attrs= {'class' : "form-group col-md-5"}),
      'documento': forms.TextInput (attrs= {'class' : "form-group col-md-3"}),
      'telefono': forms.TextInput (attrs= {'class' : "form-group col-md-3"}),
      'nacionalidad': forms.Select (attrs= {'class' : "form-group col-md-3"})
    }