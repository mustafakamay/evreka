from django.urls import include, path
from rest_framework import routers
from .views import BinOperationViewSet


router = routers.DefaultRouter()


router.register('collection-frequency', BinOperationViewSet)

app_name = 'case2'

urlpatterns = [
    path('', include(router.urls)),
]
