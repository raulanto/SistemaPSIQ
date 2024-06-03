from django.contrib import admin
from ..models.Persona import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pk_persona_curp', 'nombre', 'apellido_paterno', 'apellido_materno']

    fieldsets = (
        ('Datos Generales', {
            'fields': (
                'pk_persona_curp', 'nombre', 'apellido_paterno', 'apellido_materno', ('fk_religion', 'fk_enum_sexo'),
                ('fk_enum_tipo_sangre', 'fk_enum_estado_civil'))
        }),
        ('Nacimiento', {
            'fields': ('fk_pais_nacimiento', 'fk_municipio_nacimiento', 'otro_municipio_nacimiento')
        }),
        ('Domicilio', {
            'fields': (
                'fk_pais_vive', 'fk_codigo_postal', 'fk_cat_asentamiento', 'calle', ('numero_exterior',
                                                                                     'numero_interior'))
        }),
        ('Contacto', {
            'fields': (
                'telefono',)
        }),
        ('Otros', {
            'fields': (
                'fk_cat_escolaridad', 'habla_lengua_indigena', 'cual_lengua_indigena')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        # Si se está editando un objeto existente, hacemos la CURP de solo lectura
        if obj:
            return ['pk_persona_curp']
        # Si se está creando un nuevo objeto, no hacemos la CURP de solo lectura
        else:
            return []


    def has_module_permission(self, request):
        if request.user.groups.filter(name='Trabajador').exists():
            return False
        return super().has_module_permission(request)

    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        if request.user.groups.filter(name='Trabajador').exists():
            return {}
        return perms