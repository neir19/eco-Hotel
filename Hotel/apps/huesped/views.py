from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.huesped.models import Cliente,Nacionalidad
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.huesped.forms import NacionalidadForm, GestionForm 
from django.urls import reverse_lazy

class HuespedList(ListView):
  model=Cliente
  template_name='huesped/huesped_list.htm'

class HuespedNew(CreateView):
  model=Cliente
  form_class=GestionForm
  template_name='huesped/huesped_form.htm'
  success_url= reverse_lazy('huesped_listar')

class HuespedUpdate(UpdateView):
  model=Cliente
  form_class=GestionForm
  template_name='huesped/huesped_form.htm'
  success_url= reverse_lazy('huesped_listar')

class HuespedDelete(DeleteView):
  model=Cliente
  form_class=GestionForm
  template_name='huesped/huesped_delete.htm'
  success_url= reverse_lazy('huesped_listar')
  
class NacionalidadList(ListView):
  model = Nacionalidad
  template_name ='nacionalidad/nacionalidad_list.htm' 


class NacionalidadCreate(CreateView):
  model=Nacionalidad
  form_class= NacionalidadForm
  template_name='nacionalidad/nacionalidad_form.htm'
  success_url= reverse_lazy('huesped_listar')

class NacionalidadUpdate(UpdateView):
  model=Nacionalidad
  form_class=NacionalidadForm
  template_name='nacionalidad/nacionalidad_list.htm'
  success_url= reverse_lazy('huesped_listar')

class NacionalidadDelete(DeleteView):
  model=Nacionalidad
  form_class=NacionalidadForm
  template_name='nacionalidad/nacionalidad_delete.htm'
  success_url= reverse_lazy('huesped_listar')  