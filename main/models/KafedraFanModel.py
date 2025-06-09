from django.db import models

from main.models.FanModel import FanModel
from main.models.KafedraModel import KafedraModel
from main.models.QushimchalarModel import QushimchalarModel


class KafedraFanModel(models.Model):
    kafedra_id = models.ForeignKey(KafedraModel, on_delete=models.CASCADE)
    fan_id = models.ForeignKey(FanModel, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(QushimchalarModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(True)