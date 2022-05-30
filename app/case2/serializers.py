from rest_framework import serializers
from .models import Bin, Operation, BinOperation

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ['longitude', 'latitude']

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['name',]

class BinOperationSerializer(serializers.ModelSerializer):
    bin = BinSerializer(read_only=True)
    operation = OperationSerializer(read_only=True)
    
    class Meta:
        model = BinOperation
        fields = ['bin', 'operation', 'collection_frequency']