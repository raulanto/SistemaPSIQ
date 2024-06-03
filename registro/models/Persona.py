from django.db import models
from .TimeStampedModel import TimeStampedModel
from catalago.models import cat_tipo_asentamientos, cat_pais, cat_escolaridades, \
    cat_municipios, cat_religiones

from django.core.exceptions import ValidationError

from curp import CURP



class Persona(TimeStampedModel):
    # Datos Personales
    id = models.AutoField(primary_key=True)
    pk_persona_curp = models.CharField(max_length=18, verbose_name='Curp')
    apellido_paterno = models.CharField(max_length=30, null=True, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=30, null=True, verbose_name='Apellido Materno')
    nombre = models.CharField(max_length=40, null=True, verbose_name='Nombre')
    fecha_nacimiento = models.DateField(null=True, verbose_name='Nacimiento')
    personascol = models.CharField(max_length=45, null=True)
    fk_religion = models.ForeignKey(
        cat_religiones,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Religion'
    )

    fk_enum_sexo = models.CharField(max_length=6, choices=(('Mujer', 'Mujer'), ('Hombre', 'Hombre')), null=True,
                                    verbose_name='Sexo')
    fk_enum_tipo_sangre = models.CharField(max_length=3, choices=(
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'),
        ('O-', 'O-')),
                                           null=True,
                                           verbose_name='Tipo de sangre'
                                           )
    fk_enum_estado_civil = models.CharField(max_length=10,
                                            choices=(('Soltero(a)', 'Soltero(a)'), ('Casado(a)', 'Casado(a)')),
                                            null=True,
                                            verbose_name='Estado civil'
                                            )
    # Contacto
    telefono = models.CharField(max_length=10, null=True, verbose_name='Telefomo')

    # Nacimiento
    fk_pais_nacimiento = models.ForeignKey(
        cat_pais,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='pais_nacimiento_personas',
        verbose_name='Paiz Nacimineto'
    )

    fk_municipio_nacimiento = models.ForeignKey(
        cat_municipios,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='municipio_nacimiento_personas',
        verbose_name='Municipio'
    )

    otro_municipio_nacimiento = models.ForeignKey(
        cat_municipios,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='otro_municipio_nacimiento_personas',
        verbose_name='Segundo Municipio'
    )
    # Domicilio
    fk_pais_vive = models.ForeignKey(
        cat_pais,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='pais_vive_personas',
        verbose_name='Pais Actual'
    )

    fk_codigo_postal = models.CharField(max_length=6, null=True, verbose_name='Codigo postal')
    fk_cat_asentamiento = models.ForeignKey(
        cat_tipo_asentamientos,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Asentamiento'
    )
    calle = models.CharField(max_length=45, null=True, verbose_name='Calle')
    numero_exterior = models.CharField(max_length=10, null=True, verbose_name='Numero exterior')
    numero_interior = models.CharField(max_length=10, null=True, verbose_name='Numero Interior')
    # Escolaridad
    fk_cat_escolaridad = models.ForeignKey(cat_escolaridades, on_delete=models.CASCADE, blank=True, null=True,
                                           verbose_name='Escolaridad')

    habla_lengua_indigena = models.BooleanField(null=True, verbose_name='Lengua indigena')
    cual_lengua_indigena = models.CharField(max_length=45)

    # def clean(self):
    #     # Llama al método clean de la superclase para mantener otras validaciones
    #     super().clean()
    #
    #     # Realiza la validación de la CURP
    #     if self.pk_persona_curp:
    #         try:
    #             curp_instance = CURP(self.pk_persona_curp)
    #             if not curp_instance:
    #                 raise ValidationError({'pk_persona_curp': 'La CURP ingresada no es válida.'})
    #         except ValueError:
    #             raise ValidationError({'pk_persona_curp': 'La CURP ingresada no es válida.'})

    # class Meta:
    #     unique_together = ('pk_persona_curp',)

    def __str__(self):
        return self.pk_persona_curp
