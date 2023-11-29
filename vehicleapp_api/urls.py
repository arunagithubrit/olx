from django.urls import path
from vehicleapp_api import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('a1/vehicles',views.VehicleViewSetView,basename='a1vehicles')


urlpatterns=[

]+router.urls