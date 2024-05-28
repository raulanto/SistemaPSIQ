from django.db import models
from .Persona import Persona
from .TimeStampedModel import TimeStampedModel
from django_ckeditor_5.fields import CKEditor5Field

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Paciente(TimeStampedModel):
    foto = ProcessedImageField(
        blank=True,
        default="",
        upload_to='foto/',
        # Procesadores para redimensionar la imagen
        processors=[ResizeToFit(width=200, height=200)],
        # Formato de salida
        format='JPEG',
        # Opciones adicionales, como calidad de compresión
        options={'quality': 90}
    )
    fk_persona_curp = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name='Persona',null=True)
    ocupacion_anterior = CKEditor5Field(verbose_name='Ocupacion Anterior')
    ocupacion_actual = CKEditor5Field(verbose_name='Ocupacion Actual')

    class Meta:
        unique_together = ('fk_persona_curp',)

    def __str__(self):
        return self.fk_persona_curp.nombre