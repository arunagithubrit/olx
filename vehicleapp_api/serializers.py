from vehicleapp.models import Vehicles
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    
    
    class Meta:
        model=Vehicles
        fields="__all__"