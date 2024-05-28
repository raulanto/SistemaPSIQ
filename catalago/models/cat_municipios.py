from django.db import models
from .cat_estados import cat_estados
from .TimeStampedModel import TimeStampedModel
class cat_municipios(TimeStampedModel):
    nombre = models.CharField(max_length=45)
    fk_cat_estado = models.ForeignKey(
        cat_estados,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Estado'
    )

    def __str__(self):
        return self.nombre