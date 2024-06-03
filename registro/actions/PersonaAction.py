from django.http import HttpResponse
import csv


def download_person_data(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="person_data.csv"'

    writer = csv.writer(response)
    # Escribir encabezados
    writer.writerow(['CURP', 'Apellido Paterno', 'Apellido Materno', 'Nombre', 'Fecha de Nacimiento',
                     'Religión', 'Sexo', 'Tipo de Sangre', 'Estado Civil', 'Teléfono', 'País de Nacimiento',
                     'Municipio de Nacimiento', 'Segundo Municipio de Nacimiento', 'País de Residencia',
                     'Código Postal', 'Asentamiento', 'Calle', 'Número Exterior', 'Número Interior',
                     'Escolaridad', 'Habla Lengua Indígena', 'Cual Lengua Indígena'])

    # Escribir datos de personas
    for persona in queryset:
        writer.writerow([
            persona.pk_persona_curp, persona.apellido_paterno, persona.apellido_materno, persona.nombre,
            persona.fecha_nacimiento, persona.fk_religion, persona.fk_enum_sexo, persona.fk_enum_tipo_sangre,
            persona.fk_enum_estado_civil, persona.telefono, persona.fk_pais_nacimiento,
            persona.fk_municipio_nacimiento, persona.otro_municipio_nacimiento, persona.fk_pais_vive,
            persona.fk_codigo_postal, persona.fk_cat_asentamiento, persona.calle, persona.numero_exterior,
            persona.numero_interior, persona.fk_cat_escolaridad, persona.habla_lengua_indigena,
            persona.cual_lengua_indigena
        ])

    return response

download_person_data.short_description = "Descargar datos de personas"