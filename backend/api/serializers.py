from rest_framework import serializers
from api.models import Machine, Maintenance, Technician

class MachineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Machine
        fields = ('id', 'serial_number', 'processor_model', 'installed_ram', 'installed_storage')

class TechnicianSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Technician
        fields = ('id', 'name', 'email', 'phone_number')

class MaintenanceSerializer(serializers.ModelSerializer):
    machine = serializers.CharField(source='machine.serial_number')
    technician = serializers.CharField(source='technician.name', allow_null=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Maintenance
        fields = ('id', 'machine', 'technician', 'maintenance_date', 'maintenance_description')

    def create(self, validated_data):
        machine_serial_number = validated_data.pop('machine')['serial_number']
        technician_name = validated_data.pop('technician')['name']
        machine = Machine.objects.get(serial_number=machine_serial_number)
        technician = Technician.objects.get(name=technician_name)
        maintenance = Maintenance.objects.create(machine=machine, technician=technician, **validated_data)
        return maintenance
    
    def update(self, instance, validated_data):
        machine_serial_number = validated_data.pop('machine')['serial_number']
        technician_name = validated_data.pop('technician')['name']
        machine = Machine.objects.get(serial_number=machine_serial_number)
        technician = Technician.objects.get(name=technician_name)
        instance.machine = machine
        instance.technician = technician
        instance.maintenance_date = validated_data.get('maintenance_date', instance.maintenance_date)
        instance.maintenance_description = validated_data.get('maintenance_description', instance.maintenance_description)
        instance.save()
        return instance
    


