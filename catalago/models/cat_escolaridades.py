from django.db import models
from simple_history.models import HistoricalRecords
from .TimeStampedModel import TimeStampedModel

class cat_escolaridades(TimeStampedModel):
    nombre = models.CharField(max_length=25)


    def __str__(self):
        return self.nombre