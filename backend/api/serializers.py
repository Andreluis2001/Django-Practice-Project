from rest_framework import serializers
from api.models import Machine, Maintenance, Technician

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'serial_number', 'processor_model', 'installed_ram', 'installed_storage')

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = ('id', 'name', 'email', 'phone_number')

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('id', 'machine', 'technician', 'maintenance_date', 'maintenance_description')
