from django.db import models

class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    serial_number= models.CharField(max_length=100, unique=True) 
    processor_model = models.CharField(max_length=100)
    installed_ram = models.PositiveIntegerField()
    installed_storage = models.PositiveIntegerField()

    def __str__(self):
        return f"Machine with serial number: {self.serial_number}"
    
class Technician(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Technician: {self.name}"
    
class Maintenance(models.Model):
    id = models.AutoField(primary_key=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    maintenance_description = models.TextField()

    def __str__(self):
        return f"Machine: {self.machine} was maintained by {self.technician} on {self.maintenance_date}"
    
