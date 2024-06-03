from django.contrib import admin
from ..models import Paciente,Persona
from django import forms
from imagekit.admin import AdminThumbnail





@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['id','admin_thumbnail', 'fk_persona_curp']


    fieldsets = (
        ('Paciente', {
            'fields': ('foto','fk_persona_curp',)
        }),
        ('Ocupacion', {
            'fields': ('ocupacion_anterior','ocupacion_actual',)
        }),

    )
    admin_thumbnail = AdminThumbnail(image_field='foto')


