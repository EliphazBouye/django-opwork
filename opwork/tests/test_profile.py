from django.test import TestCase
from http import HTTPStatus

class TestProfileView(TestCase):
    def test_get_profile_view_if_user_not_auth(self):
        response = self.client.get("/accounts/profile/")
        
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], '/accounts/login/?redirect_to=/accounts/profile/')