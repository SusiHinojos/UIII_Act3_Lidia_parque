from django.db import models

class Empleado(models.Model):
    id_emp = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=40)
    telefono = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    id_atr = models.IntegerField()

    def __str__(self):
        return self.nombre