from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
  class Meta:
    model = User
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
    ]

    labels = {
      'username': 'Nombre de usurio',
      'first_name': 'Nombre',
      'last_name': 'Apellido',
      'email': 'Email',
    }

    # widgets = {
    #   'username': 'Nombre de usurio',
    #   'first_name': 'Primer nombre',
    #   'last_name': 'Apellido',
    #   'email': 'email',
    # }
