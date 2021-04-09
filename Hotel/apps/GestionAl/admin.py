from django.contrib import admin
from apps.GestionAl.models import  Estado, Registrador, Alquiler 

# Register your models here.

admin.site.register(Registrador)
admin.site.register(Estado)
admin.site.register(Alquiler)
