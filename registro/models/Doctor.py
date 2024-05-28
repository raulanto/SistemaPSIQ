from django.contrib.auth.models import User
from django.db import models
from .TimeStampedModel import TimeStampedModel



class Doctor(TimeStampedModel):
    numero_cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=255)
    profesion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre
