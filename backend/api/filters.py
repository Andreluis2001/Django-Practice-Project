import django_filters
from api.models import Machine, Maintenance

class MachineFilter(django_filters.FilterSet):
    class Meta:
        model = Machine
        fields = {
            'serial_number' : ['exact'],
            'processor_model' : ['icontains'],
        }

class MaintenanceFilter(django_filters.FilterSet):
    class Meta:
        model = Maintenance
        fields = {
            'machine__serial_number' : ['exact'],
            'technician__name' : ['icontains'],
        }