from django.db import models

class TarkibTuriModel(models.Model):
    name = models.CharField(max_length=100)
    izoh = models.TextField()

    def __str__(self):
        return str(True)