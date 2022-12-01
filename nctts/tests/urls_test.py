from django.test import SimpleTestCase
from django.urls import reverse, resolve
from operatorview.views import Escalated, ManageRep, searchresults

class URLTest(SimpleTestCase):

    def test_url_resolves(self):
        url = reverse("Escalated")
        print(resolve(url))
        self.assertEquals(resolve(url.func, Escalated))

    def test_ManageReports_url_resolves(self):
        url = reverse("ManageReports")
        print(resolve(url))
        self.assertEquals(resolve(url.func, ManageRep))

    def test_searchresults_url_resolves(self):
        url = reverse("searchresults")
        print(resolve(url))
        self.assertEquals(resolve(url.func, searchresults))