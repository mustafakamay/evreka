from django.db import models


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()



class Operation(models.Model):
    name = models.CharField(max_length=120)



class BinOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name="operation_bins")
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name="bin_operations")
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField()

