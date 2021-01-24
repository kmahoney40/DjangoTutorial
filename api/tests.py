from django.test import TestCase
from .models import Bucketlist
from water.models import RunTimes, Temp
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

        """Add a row to RunTimes temp table"""
        self.v1 = 1
        self.v2 = 2
        self.v3 = 3
        self.v4 = 4
        self.v5 = 5
        self.v6 = 6
        self.v7 = 7
        self.day = 0
        self.runtimes = RunTimes(v1=self.v1, v2=self.v2, v3=self.v3, v4=self.v4, v5=self.v5, v6=self.v6, v7=self.v7, day=self.day)
        
        """Add a row to the temp Temp table"""
        self.t1 = 1.1
        self.t2 = 2.2
        self.t3 = 3.3
        self.t4 = 4.4
        self.t5 = 5.5
        self.temp = Temp(t1=self.t1, t2=self.t2, t3=self.t3, t4=self.t4, t5=self.t5)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
        
    def test_model_can_create_a_runtimes(self):
        old_count = RunTimes.objects.count()
        self.runtimes.save()
        new_count = RunTimes.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_temp(self):
        old_count = Temp.objects.count()
        self.temp.save()
        new_count = Temp.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")
        
        self.runtimes_data = {'v1':1, 'v2':2, 'v3':3, 'v4':4, 'v5':5, 'v6':6, 'v7':7, 'day':0}
        self.runtimes_response = self.client.post(
            reverse('createruntimes'),
            self.runtimes_data,
            format="json")
        
        self.temp_data = {'t1':1.1,'t2':1.2,'t3':1.3,'t4':1.4,'t5':1.5}
        self.temp_response = self.client.post(
            reverse('createtemp'),
            self.temp_data,
            format="json")
        
    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': bucketlist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = Bucketlist.objects.first()
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_create_a_temp(self):
        '''Test the api can create a row in Temp table'''
        self.assertEqual(self.temp_response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_create_a_runtimes(self):
        self.assertEqual(self.runtimes_response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_update_a_runtimes(self):
        runtime = RunTimes.objects.order_by('day').first()
        runtimes_data = {'day':1}
        response = self.client.put(
            reverse('detailsruntimes', kwargs={'pk':runtime.id}),
            runtimes_data,
            format='json'
            )
        runtime = RunTimes.objects.order_by('day').first()
        self.assertEqual(runtime.day, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
