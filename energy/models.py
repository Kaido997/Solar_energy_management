from django.db import models
from django.utils.timezone import now


class Solar_energy(models.Model):
    time = models.DateTimeField(default=now)
    produced = models.IntegerField(null=True)
    consumed = models.IntegerField(null=True)
    transactionID = models.CharField(max_length=32, default=None, null=True)

    def __str__(self):
        return self.time.strftime('%Y-%m-%d %H:%M')

   

# Create your models here.
