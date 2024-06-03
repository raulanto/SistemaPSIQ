from django.contrib import admin
from ..models import Trabajador



@admin.register(Trabajador)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido_paterno', 'apellido_materno', 'activo', 'fk_doctor', 'usuario')