from django.contrib.auth.models import User
from rest_framework import serializers
from vehicleapp2.models import Vehicles



class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","password","email"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class VehicleSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)

    class Meta:
        model=Vehicles
        fields="__all__"