from django.urls import path
from vehicleapp2_api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('vehicles',views.VehicleViewsetView,basename='vehicles')

urlpatterns=[
    path('a1/signup/',views.UserCreationView.as_view())
]+router.urls