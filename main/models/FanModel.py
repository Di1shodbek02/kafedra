from django.db import models

from main.models.KafedraModel import KafedraModel


class FanModel(models.Model):
    name = models.CharField(max_length=100)
    talim_yunalishi = models.CharField(max_length=100)
    kafedra = models.ForeignKey(KafedraModel, on_delete=models.CASCADE, related_name='fanlar')



    def __str__(self):
        return self.name
