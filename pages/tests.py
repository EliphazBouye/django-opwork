from django.test import TestCase
from http import HTTPStatus

class PagesTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        
        self.assertEqual(response.status_code, HTTPStatus.OK)