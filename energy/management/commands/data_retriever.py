from django.core.management.base import BaseCommand, CommandError
from energy.models import Solar_energy
from energy.secret import URL
from energy.model_utils import get_data_from_endpoint, makeTransaction
from time import sleep
import hashlib

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            data = get_data_from_endpoint(URL)
            _hash = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
            tx = makeTransaction(_hash)
            sleep(10)
            new = Solar_energy(produced=data['produced_energy_in_watt'], consumed=data['consumed_energy_in_watt'], transactionID=tx)
            new.save() 
        except ValueError:
            raise CommandError("Error creating transaction")

