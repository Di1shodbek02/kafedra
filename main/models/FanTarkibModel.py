from django.db import models

from main.models.FanModel import FanModel
from main.models.TarkibTuriModel import TarkibTuriModel


class FanTarkibModel(models.Model):
    fan_id = models.ForeignKey(FanModel, on_delete=models.CASCADE)
    tarkib_tur_id = models.ForeignKey(TarkibTuriModel, on_delete=models.CASCADE)
    soat = models.CharField(max_length=255)

    def __str__(self):
        return str(True)