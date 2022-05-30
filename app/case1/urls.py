from django.urls import include, path
from rest_framework import routers
from .views import NavigationRecordViewSet,VehicleViewSet


router = routers.DefaultRouter()

router.register('last-points', NavigationRecordViewSet)
router.register('vehicle', VehicleViewSet)
app_name = 'case1'

urlpatterns = [
    path('', include(router.urls)),
]
