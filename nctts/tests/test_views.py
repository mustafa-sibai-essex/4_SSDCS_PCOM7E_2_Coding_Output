from django.test import TestCase, Client
from django.urls import reverse
from report.models import PublicUser, Vulnerabilities
import json

class TestView(TestCase):
    
    def test_report_POST(self):
        
        client = Client()
        
        response = client.post(reverse('POST'))
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'nctts/')