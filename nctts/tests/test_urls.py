import unittest
from django.test import TestCase
from django.urls import reverse, resolve
from homepage.views import login_user, login_success, login_failed
from django import setup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nctts.settings")
setup()

#Checking to test if homepage url is called and runs with no errors.
class TestsUrls(unittest.TestCase):

    def tests_login_user(self):
        url = reverse('homepage:login_user')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_user)
            
    def tests_login_success(self):
        url = reverse('homepage:login_success')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_success)
        
    def tests_login_failed(self):
        url = reverse('homepage:login_failed')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_failed)