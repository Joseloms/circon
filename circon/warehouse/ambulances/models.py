from django.db import models


class Ambulances(models.Model):
    ambulances = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.ambulances
