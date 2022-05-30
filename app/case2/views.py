from rest_framework import viewsets

from .serializers import BinOperationSerializer
from .models import BinOperation


class BinOperationViewSet(viewsets.ModelViewSet):
    queryset = BinOperation.objects.all()
    serializer_class = BinOperationSerializer