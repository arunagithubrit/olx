from django.shortcuts import render,redirect
from django.views.generic import View
from vehicleapp.forms import VehicleCreateForm,VehicleChangeForm,RegistrationForm,LoginForm
from vehicleapp.models import Vehicles
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.



class VehicleCreateView(View):
    def get(self,request,*args,**kwargs):
        form=VehicleCreateForm()
        return render(request,"vehicle_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=VehicleCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # Vehicles.objects.create(**form.cleaned_data)
            print("vehicle added")
            return render(request,"vehicle_add.html",{"form":form})
        else:
            return render(request,"vehicle_add.html",{"form":form})
        
class VehicleListView(View):
    def get(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        return render(request,"vehicle_list.html",{"vehicles":qs})


        

class VehicleDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicles.objects.get(id=id)
        return render(request,"vehicle_detail.html",{"vehicle":qs})






class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Vehicles.objects.filter(id=id).delete()
        return redirect("vehicle-list")





class VehicleUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Vehicles.objects.get(id=id)
        form=VehicleChangeForm(instance=obj)
        return render(request,"vehicle_edit.html",{"form":form})

    def post(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            obj=Vehicles.objects.get(id=id)
            form=VehicleChangeForm(request.POST,instance=obj,files=request.FILES)
            if form.is_valid():
                 form.save()
                 return redirect("vehicle-list")
            else:
                return render(request,"vehicle_edit.html",{"form":form})
         

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("register")
        else:
            return render(request,"registration.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("vehicle-list")
            else:
                return render(request,"login.html",{"form":form})

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
        

    
    

        

    

    

