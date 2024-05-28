from django.db import models
from .TimeStampedModel import TimeStampedModel

class cat_religiones(TimeStampedModel):
    nombre = models.CharField(max_length=30)



    def __str__(self):
        return self.nombre