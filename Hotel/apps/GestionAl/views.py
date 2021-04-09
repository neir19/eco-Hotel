from django.shortcuts import render
from django.http import HttpResponse
from apps.GestionAl.models import Alquiler
from apps.GestionAl.form import AlquilerForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return HttpResponse("index")

class AlquilerList(ListView):
    model=Alquiler
    template_name='Alquiler/Alquiler_list.html'

class AlquilerCreate(CreateView):
    model=Alquiler
    form_class = AlquilerForm
    template_name='Alquiler/Alquiler_form.html'
    success_url = reverse_lazy('Alquiler_listar')

class AlquilerUpdate(UpdateView):
    model=Alquiler
    form_class = AlquilerForm
    template_name='Alquiler/Alquiler_form.html'
    success_url = reverse_lazy('Alquiler_listar')

class AlquilerDelete(DeleteView):
    model=Alquiler
    template_name='Alquiler/Alquiler_delete.html'
    success_url = reverse_lazy('Alquiler_listar')




















































# def Alquiler_list(request):
#   GestionAl=Alquiler.objects.all().order_by('fechaHoraEntrada')
#   contexto={'Alquileres':Alquiler}
#   return render(request,'Alquiler/Alquiler_list.html',contexto)

# def Alquiler_new(request):
#   if request.method == 'POST':
#     form=AlquilerForm(request.POST)
#     if form.is_valid():
#       form.save()
#     return redirect('Alquiler_listar')
#   else:
#     form=AlquilerForm()
#   return render(request, 'Alquiler/Alquiler_form.html', {'form': form})

# def Alquiler_edit(request, id_Alquiler):
#   GestionAl =Alquiler.objects.get(id=id_Alquiler)
#   if request.method == 'GET':
#     form=AlquilerForm(instance=Alquiler)
#   else:
#     form=AlquilerForm(request.POST,instance=Alquiler)
#     if form.is_valid():
#       form.save()
#     return redirect('Alquiler_listar')
#   return render(request, 'Alquiler/Alquiler_form.html',{'form':form})

# def Alquiler_delete(request, id_Alquiler):
#   GestionAl =Alquiler.objects.get(id=id_Alquiler)
#   if(request.method=='POST'):
#     Alquiler.delete()
#     return redirect('Alquiler_listar')
#   return render(request, 'Alquiler/Alquiler_delete.html',{'Alquiler':Alquiler})

