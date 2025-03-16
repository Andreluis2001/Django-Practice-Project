from rest_framework import generics
from api.models import Machine, Maintenance, Technician
from api.serializers import MachineSerializer, MaintenanceSerializer, TechnicianSerializer
from api.filters import MachineFilter

class MachineListAPIView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filterset_class = MachineFilter

class MachineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class TechnicianListAPIView(generics.ListCreateAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer

class TechnicianDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    
class MaintenanceListAPIView(generics.ListCreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

class MaintenanceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
