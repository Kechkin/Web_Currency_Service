import requests
from django.test import TestCase
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Webconverter.settings")
django.setup()
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_conv_to(self):
        c = Client()
        response = c.post('/converterTo/', {'currency': 'Евро', 'rub': '444'})
        self.assertEqual(response.status_code, 200)

    def test_conv_From(self):
        c = Client()
        response = c.post('/converterFrom/', {'currency': 'Евро', 'money': '14.5'})
        self.assertEqual(response.status_code, 200)
