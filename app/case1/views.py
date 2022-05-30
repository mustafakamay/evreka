from datetime import datetime, timedelta
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import viewsets
from .models import NavigationRecord,Vehicle
from .serializers import NavigationRecordSerializer,VehicleSerializer
from django.utils import timezone

class NavigationRecordViewSet(viewsets.ModelViewSet):

    queryset = NavigationRecord.objects.all()
    serializer_class = NavigationRecordSerializer

    def list(self, request, *args, **kwargs):
        last_two_days = timezone.now() - timezone.timedelta(days=2)
        queryset = NavigationRecord.objects.filter(datetime__range=(last_two_days.date(), timezone.now()))
        serializer = NavigationRecordSerializer(queryset, many=True)
        
        return Response(serializer.data, status=200)

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer