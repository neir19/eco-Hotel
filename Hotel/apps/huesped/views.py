from django.shortcuts import render
from apps.huesped.models import Cliente
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .form import GestionForm
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