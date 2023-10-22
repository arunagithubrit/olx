

# Create your views here.
from django.shortcuts import render,redirect
from vehicleapp2.forms import RegistrationForm,LoginForm,VehicleCreateForm,VehicleChangeForm
from django.views.generic import View,TemplateView,FormView,ListView,DetailView,UpdateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from vehicleapp2.models import Vehicles
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper



class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration succesfully completed")
            return redirect("signin")
        else:
            messages.error(request,"failed to created account")
            return render(request,"signup.html",{"form":form})
        


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
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials!!!!")
                return render(request,"login.html",{"form":form})



@method_decorator(signin_required,name="dispatch")            
class IndexView(TemplateView):
    template_name="index.html"


@method_decorator(signin_required,name="dispatch")
class VehicleCreateView(FormView):
    template_name="vehicleapp2/vehicle_add.html"
    form_class=VehicleCreateForm
    
    def post(self,request,*args,**kwargs):
        form=VehicleCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            # form.save()
            messages.success(request,"Vehicle added successfully")
            Vehicles.objects.create(**form.cleaned_data,user=request.user)
            return redirect("add-vehicle")
        else:
            messages.error(request,"Unable to Add")
            return render(request,"vehicleapp2/vehicle_add.html",{"form":form})
            


@method_decorator(signin_required,name="dispatch")        
class VehicleListView(ListView):
    template_name="vehicleapp2/vehicle_list.html"
    context_object_name="vehicles"
    model=Vehicles
    
    def get_queryset(self):
        qs= Vehicles.objects.filter(user=self.request.user)
        return qs
    

@method_decorator(signin_required,name="dispatch")
class VehicleDetailView(DetailView):
    template_name="vehicleapp2/vehicle_detail.html"
    context_object_name="vehicle"
    model=Vehicles




@method_decorator(signin_required,name="dispatch")
class VehicleUpdateView(UpdateView):
    template_name="vehicleapp2/vehicle_edit.html"
    form_class=VehicleChangeForm
    model=Vehicles
    success_url=reverse_lazy("list-vehicle")

 

@signin_required
def remove_vehicle(request,*args,**kwargs):
    id=kwargs.get("pk")
    Vehicles.objects.filter(id=id).delete()
    return redirect("list-vehicle")



