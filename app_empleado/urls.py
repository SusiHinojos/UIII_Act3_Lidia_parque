from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('ver/', views.ver_empleados, name='ver_empleados'),
    path('actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('realizar_actualizacion/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
]
