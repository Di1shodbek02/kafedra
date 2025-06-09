from django.db import models

from main.models.FanTarkibModel import FanTarkibModel


class FanTarkibMavzuModel(models.Model):
    fan_tarkib_id = models.ForeignKey(FanTarkibModel, on_delete=models.CASCADE)
    mavzu_nomi = models.CharField(max_length=255)
    mavzu_tili = models.CharField(max_length=255)
    asos_file = models.FileField(upload_to='pics')