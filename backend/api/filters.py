import django_filters
from api.models import Machine 

class MachineFilter(django_filters.FilterSet):
    class Meta:
        model = Machine
        fields = {
            'serial_number' : ['exact'],
            'processor_model' : ['icontains'],
        }