from django.db import models


class Currencies(models.Model):

    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=3)
    quantity = models.IntegerField(default=0)
    tobgn = models.FloatField(default=0.0)
    frombgn = models.FloatField(default=0.0)

    def __str__(self):
        return self.name + ' : ' + self.shortname

