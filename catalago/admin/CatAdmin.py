from django.contrib import admin
from ..models import *
from ..models.cat_asentamientos import cat_asentamientos
from ..models.cat_escolaridades import cat_escolaridades
from ..models.cat_estados import cat_estados
from ..models.cat_municipios import cat_municipios
from ..models.cat_pais import cat_pais
from ..models.cat_religiones import cat_religiones
from ..models.cat_tipo_asentamientos import cat_tipo_asentamientos


@admin.register(cat_asentamientos)
class cat_asentamientosAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.groups.filter(name__in=['Trabajador', 'Doctor']).exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms


@admin.register(cat_pais)
class cat_paisAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.groups.filter(name__in=['Trabajador', 'Doctor']).exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms


@admin.register(cat_tipo_asentamientos)
class cat_tipo_asentamientosAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.groups.filter(name__in=['Trabajador', 'Doctor']).exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms


@admin.register(cat_estados)
class cat_estadosAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.groups.filter(name__in=['Trabajador', 'Doctor']).exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms


@admin.register(cat_religiones)
class cat_religionesAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.groups.filter(name__in=['Trabajador', 'Doctor']).exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms


@admin.register(cat_escolaridades)
class cat_escolaridadesAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.groups.filter(name__in=['Trabajador', 'Doctor']).exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms


@admin.register(cat_municipios)
class cat_municipiosAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.groups.filter(name__in=['Trabajador', 'Doctor']).exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms
