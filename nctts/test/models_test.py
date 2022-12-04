from django.test import TestCase
from report.models import Vulnerabilities
from operatorview.models import PublicUser



class TestModels(TestCase):
    def setUp(self):
        Vulnerabilities.objects.create(name="status")
        Vulnerabilities.objects.create(name="description")

    def test_report_models(self):
        status = Vulnerabilities.objects.create(name="status")
        description = Vulnerabilities.objects.create(name="description")
        self.assertEqual(str(Vulnerabilities), "status")
        self.assertEqual(str(Vulnerabilities), "description")

    def test_operator_models(self):
        PublicUser.objects.create(name="first_name")
        PublicUser.objects.create(name="email")