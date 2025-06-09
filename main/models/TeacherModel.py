from django.db import models

from main.models.KafedraModel import KafedraModel


class TeacherModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    kafedra_id = models.ForeignKey(KafedraModel, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name
