from time import sleep
from django.db import models
from energy.model_utils import makeTransaction, get_data_from_endpoint
from django.utils.timezone import now
from energy.secret import URL
import hashlib

class Solar_energy(models.Model):
    time = models.DateTimeField(default=now)
    produced = models.IntegerField(null=True)
    consumed = models.IntegerField(null=True)
    transactionID = models.CharField(max_length=32, default=None, null=True)

    def newData(self):
        data = get_data_from_endpoint(URL)
        _hash = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        tx = makeTransaction(_hash)
        new = Solar_energy(produced=data['produced_energy_in_watt'], consumed=data['consumed_energy_in_watt'], transactionID=tx)
        new.save()
        sleep(5)
       
    def __str__(self):
        return self.time.strftime('%Y-%m-%d %H:%M')

   

# Create your models here.
