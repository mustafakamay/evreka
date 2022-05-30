from django.test import TestCase
from .serializers import NavigationRecordSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import NavigationRecord, Vehicle
import datetime


class NavigationRecordApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @classmethod
    def setUpTestData(cls):
        cls.vehicle = Vehicle.objects.create(plate="34 KMY 02")
        cls.navigation_record = NavigationRecord.objects.create(
            latitude="02.02",
            longitude="34.34",
            vehicle = cls.vehicle,
            datetime = datetime.datetime(2022, 5, 30, 2, 8, 25, 325848)
        )
    
    def test_navigation_record(self):
        navigation_record = NavigationRecord(
            latitude="02.02",
            longitude="34.34",
            vehicle = self.vehicle,
            datetime = datetime.datetime(2022, 5, 30, 2, 8, 25, 325848)
        )
        self.assertEqual(navigation_record.latitude, "02.02")
        self.assertEqual(navigation_record.longitude, "34.34")
        self.assertEqual(navigation_record.vehicle.plate, self.vehicle.plate)
        self.assertEqual(navigation_record.datetime, datetime.datetime(2022, 5, 30, 2, 8, 25, 325848))
    

    def test_access_navigation_record_url(self):
        res = self.client.get("http://localhost:8000/last-points/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(NavigationRecord.objects.all().count(), 1)
    
    
    def test_get_last_points(self):
        old_navigation_record = NavigationRecord(
            latitude="02.02",
            longitude="34.34",
            vehicle = self.vehicle,
            datetime = datetime.datetime(2022, 5, 30, 2, 8, 25, 325848)
        )
        self.assertEqual(NavigationRecord.objects.all().count(), 1)


class VehicleModelTest(TestCase):
    def test_vehicle(self):
        vehicle = Vehicle.objects.create(plate="34 KMY 02")
        self.assertEqual(vehicle.plate, "34 KMY 02")
        self.assertEqual(Vehicle.objects.all().count(), 1)