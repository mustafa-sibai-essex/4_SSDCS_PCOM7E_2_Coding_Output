from django.test import TestCase, Client
from django.http import HttpRequest
from django.urls import reverse


class TestViews(TestCase):
    
    def test_send_mail_GET(self):
        client = Client()