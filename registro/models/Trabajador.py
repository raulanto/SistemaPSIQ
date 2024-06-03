from django.db import models
from .TimeStampedModel import TimeStampedModel

from .Doctor import Doctor
from django.contrib.auth.models import User



class Trabajador(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    pk_trabajador_curp = models.CharField(max_length=18, verbose_name='Curp')
    apellido_paterno = models.CharField(max_length=30, null=True, verbose_name='Apellido Paterno',default='')
    apellido_materno = models.CharField(max_length=30, null=True, verbose_name='Apellido Materno',default='')
    nombre = models.CharField(max_length=40, null=True, verbose_name='Nombre')
    activo = models.BooleanField(null=True)
    fk_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True,verbose_name="Doctor")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Usuario')

    class Meta:
        unique_together = ( 'usuario',)

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.nombre}"
