from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.habitacion.models import Habitacion
from apps.habitacion.form import HabitacionForm


# Create your views here.
def index(request):
  return HttpResponse("index")

def habitacion_list(request):
  habitacion=Habitacion.objects.all().order_by('numero')
  contexto={'habitaciones':habitacion}
  return render(request,'habitacion/habitacion_list.html',contexto)

def habitacion_new(request):
  if request.method == 'POST':
    form=HabitacionForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('habitacion_listar')
  else:
    form=HabitacionForm()
  return render(request, 'habitacion/habitacion_form.html', {'form': form})

def habitacion_edit(request, id_habitacion):
  habitacion =Habitacion.objects.get(id=id_habitacion)
  if request.method == 'GET':
    form=HabitacionForm(instance=habitacion)
  else:
    form=HabitacionForm(request.POST,instance=habitacion)
    if form.is_valid():
      form.save()
    return redirect('habitacion_listar')
  return render(request, 'habitacion/habitacion_form.html',{'form':form})

def habitacion_delete(request, id_habitacion):
  habitacion =Habitacion.objects.get(id=id_habitacion)
  if(request.method=='POST'):
    habitacion.delete()
    return redirect('habitacion_listar')
  return render(request, 'habitacion/habitacion_delete.html',{'habitacion':habitacion})
