from django.test import TestCase
from django.urls import reverse

class ViewsTestCase(TestCase):
    def setUp(self):
        self.url = reverse('create_post')

    def test_response_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)