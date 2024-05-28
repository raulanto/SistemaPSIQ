from ..models.Doctor import Doctor
from django.contrib import admin



@admin.register(Doctor)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['nombre','numero_cedula','profesion','telefono']