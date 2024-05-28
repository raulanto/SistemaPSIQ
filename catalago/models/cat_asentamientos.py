from django.db import models
from simple_history.models import HistoricalRecords
from .cat_tipo_asentamientos import cat_tipo_asentamientos
from .TimeStampedModel import TimeStampedModel

class cat_asentamientos(TimeStampedModel):
    nombre = models.CharField(max_length=60)
    fk_cat_tipo_asentamientos= models.ForeignKey(cat_tipo_asentamientos,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.nombre