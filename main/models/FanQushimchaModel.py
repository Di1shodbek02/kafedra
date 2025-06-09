from django.db import models

from main.models.FanModel import FanModel
from main.models.QushimchalarModel import QushimchalarModel


class FanQushimchaModel(models.Model):
    name = models.CharField(max_length=100)
    fan_id = models.ForeignKey(FanModel, on_delete=models.CASCADE)
    fan_qushimcha_id = models.ForeignKey(QushimchalarModel, on_delete=models.CASCADE)
    asos_nomi = models.CharField(max_length=100)
    asos_file = models.FileField(upload_to='pics')