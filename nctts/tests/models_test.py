from django.test import TestCase
from report.models import Vulnerabilities



class TestModels(TestCase):

    def test_basic_model_string(self):
        status = Vulnerabilities.objects.create(title="Waiting Approval")
        description = Vulnerabilities.objects.create(description="Put description here")
        self.assertEqual(str(Vulnerabilities), "Waiting Approval")

    def test_vulnerable_website(self):
        pass