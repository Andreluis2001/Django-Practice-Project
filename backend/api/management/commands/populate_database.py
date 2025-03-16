from django.core.management.base import BaseCommand
from api.models import Machine

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **kwargs):

        machines = [
            Machine(serial_number='123456', processor_model='Intel Core i7', installed_ram=16, installed_storage=512),
            Machine(serial_number='654321', processor_model='Intel Core i5', installed_ram=8, installed_storage=256),
            Machine(serial_number='135246', processor_model='Intel Core i3', installed_ram=4, installed_storage=128),
            Machine(serial_number='246135', processor_model='Intel Core i9', installed_ram=32, installed_storage=1024),
            Machine(serial_number='789012', processor_model='AMD Ryzen 7', installed_ram=16, installed_storage=512),
            Machine(serial_number='890123', processor_model='AMD Ryzen 5', installed_ram=8, installed_storage=256),
            Machine(serial_number='901234', processor_model='AMD Ryzen 3', installed_ram=4, installed_storage=128),
            Machine(serial_number='012345', processor_model='Intel Xeon', installed_ram=64, installed_storage=2048),
            Machine(serial_number='567890', processor_model='Intel Pentium', installed_ram=2, installed_storage=64),
            Machine(serial_number='678901', processor_model='Intel Celeron', installed_ram=2, installed_storage=32),
            Machine(serial_number='789012', processor_model='AMD Athlon', installed_ram=4, installed_storage=128),
            Machine(serial_number='890123', processor_model='AMD FX', installed_ram=8, installed_storage=256),
            Machine(serial_number='901234', processor_model='Intel Core M', installed_ram=8, installed_storage=256),
            Machine(serial_number='012345', processor_model='Intel Atom', installed_ram=2, installed_storage=32),
            Machine(serial_number='123456', processor_model='AMD E-Series', installed_ram=4, installed_storage=128)
        ]

        Machine.objects.bulk_create(machines)
        