from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from vehicleapp_api.serializers import VehicleSerializer
from vehicleapp.models import Vehicles

# Create your views here.


class VehicleViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        serializer=VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Vehicles.objects.get(id=id)

        serializer=VehicleSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicles.objects.get(id=id)
        serializer=VehicleSerializer(qs)
        return Response(data=serializer.data)
       
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Vehicles.objects.filter(id=id).delete()
        return Response(data={"message":"vehicle deleted"})