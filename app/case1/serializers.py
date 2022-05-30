from .models import NavigationRecord,Vehicle
from rest_framework import serializers

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'plate']

class NavigationRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavigationRecord
        fields = ['vehicle', 'datetime', 'latitude', 'longitude']

