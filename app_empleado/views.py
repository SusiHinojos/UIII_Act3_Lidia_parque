from django.shortcuts import render, redirect
from .models import Empleado

# Página de inicio
def inicio(request):
    return render(request, "inicio.html")

# Agregar empleado
def agregar_empleado(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        puesto = request.POST.get("puesto")
        telefono = request.POST.get("telefono")
        salario = request.POST.get("salario")
        id_atr = request.POST.get("id_atr")

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            telefono=telefono,
            salario=salario,
            id_atr=id_atr
        )
        return redirect("ver_empleados")

    return render(request, "empleado/agregar_empleado.html")

# Ver empleados
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "empleado/ver_empleados.html", {"empleados": empleados})

# Actualizar empleado
def actualizar_empleado(request, id):
    empleado = Empleado.objects.get(id_emp=id)
    return render(request, "empleado/actualizar_empleado.html", {"empleado": empleado})

# Realizar actualización
def realizar_actualizacion_empleado(request, id):
    empleado = Empleado.objects.get(id_emp=id)
    empleado.nombre = request.POST.get("nombre")
    empleado.apellido = request.POST.get("apellido")
    empleado.puesto = request.POST.get("puesto")
    empleado.telefono = request.POST.get("telefono")
    empleado.salario = request.POST.get("salario")
    empleado.id_atr = request.POST.get("id_atr")
    empleado.save()
    return redirect("ver_empleados")

# Borrar empleado
def borrar_empleado(request, id):
    empleado = Empleado.objects.get(id_emp=id)
    empleado.delete()
    return redirect("ver_empleados")
