from django.core.management.base import BaseCommand, CommandError
from energy.models import Solar_energy
from energy.secret import URL
from energy.model_utils import get_data_from_endpoint
from energy.model_utils import ethTestnet
import hashlib

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            data = get_data_from_endpoint(URL)
            _hash = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
            send = ethTestnet(_hash)
            try:
                tx = send.makeTransaction()
            except:
                new = Solar_energy(produced=data['produced_energy_in_watt'], consumed=data['consumed_energy_in_watt'], transactionID="PENDING")
                new.save()
                try:
                    tr = send.checkTransaction() #check if the transaction is approved for 2 minutes
                    up = Solar_energy.objects.latest('time')
                    up.transactionID = str(tr)
                    up.save()
                except: #if the transaction is not approved after 2 minutes make a new transaction with the same values as the last db object created
                    obj = Solar_energy.objects.latest('time')
                    retrydata = dict(produced_energy_in_watt = obj.produced, consumed_energy_in_watt = obj.consumed)
                    retryhash = hashlib.sha256(str(retrydata).encode('utf-8')).hexdigest()
                    retry = ethTestnet(retryhash)
                    retrytx = retry.makeTransaction()
                    obj.transactionID = str(retrytx)
                    obj.save()
            else:
                new = Solar_energy(produced=data['produced_energy_in_watt'], consumed=data['consumed_energy_in_watt'], transactionID=tx)
                new.save() 
        except ValueError:
            raise CommandError("Error creating transaction")

