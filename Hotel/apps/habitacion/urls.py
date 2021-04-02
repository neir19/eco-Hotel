from django.conf.urls import url
from apps.habitacion.views import index, HabitacionList,HabitacionDelete, HabitacionUpdate,HabitacionNew,ThabitacionNew,ThabitacionList,ThabitacionUpdate, ThabitacionDelete

urlpatterns =[
  url(r'^$',index),
  url(r'^listar/',HabitacionList.as_view(),name="habitacion_listar"),
  url(r'^nuevo/',HabitacionNew.as_view(),name="habitacion_new"),
  url(r'^editar/(?P<pk>\d+)/',HabitacionUpdate.as_view(), name="habitacion_editar"),
  url(r'^delete/(?P<pk>\d+)/',HabitacionDelete.as_view(), name="habitacion_eliminar"),
  url(r'^tnuevo/',ThabitacionNew.as_view(),name="thabitacion_new"),
  url(r'^tlistar/',ThabitacionList.as_view(),name="thabitacion_Listar"),
  url(r'^teditar/(?P<pk>\d+)/',ThabitacionUpdate.as_view(), name="thabitacion_editar"),
  url(r'^tdelete/(?P<pk>\d+)/',ThabitacionDelete.as_view(), name="thabitacion_eliminar"),
  
]