from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.habitacion.models import Habitacion, TipoHabitacion
from apps.habitacion.form import HabitacionForm, ThabitacionForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
  return HttpResponse("index")

def habitacion_delete(request, id_habitacion):
  habitacion =Habitacion.objects.get(id=id_habitacion)
  if(request.method=='POST'):
    habitacion.delete()
    return redirect('habitacion_listar')
  return render(request, 'habitacion/habitacion_delete.html',{'habitacion':habitacion})


class HabitacionList(ListView):
  model= Habitacion
  template='habitacion/habitacion_list.html'
class HabitacionNew(CreateView):
  model= Habitacion
  form_class=HabitacionForm
  template_name='habitacion/habitacion_form.html'
  success_url= reverse_lazy('habitacion_listar')
class HabitacionUpdate(UpdateView):
  model= Habitacion
  form_class=HabitacionForm
  template_name='habitacion/habitacion_form.html'
  success_url= reverse_lazy('habitacion_listar')

class HabitacionDelete(DeleteView):
  model=Habitacion
  template_name='habitacion/habitacion_delete.html'
  success_url= reverse_lazy('habitacion_listar')

class ThabitacionNew(CreateView):
  model=TipoHabitacion
  form_class= ThabitacionForm
  template_name='habitacion/habitacion_form.html'
  success_url= reverse_lazy('thabitacion_listar')
  
class ThabitacionList(ListView):
  model= TipoHabitacion
  template='Habitacion/tipoHabitacion_list.html' 

class ThabitacionUpdate(UpdateView):
  model= TipoHabitacion
  form_class=ThabitacionForm
  template_name='habitacion/habitacion_form.html'
  success_url= reverse_lazy('thabitacion_listar')

class ThabitacionDelete(DeleteView):
  model=TipoHabitacion
  template_name='habitacion/tipoHabitacion_delete.html'
  success_url= reverse_lazy('thabitacion_listar')
