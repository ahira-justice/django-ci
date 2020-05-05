from django.test import TestCase, Client
from django.urls import reverse


INDEX_URL = reverse('core:home')


class ViewTests(TestCase):
    def setUp(self):
        """Setup test client"""
        self.client = Client()

    def test_get_request(self):
        """Test default page is successfully recieved"""
        response = self.client.get(INDEX_URL)
        self.assertEqual(response.status_code, 200)
