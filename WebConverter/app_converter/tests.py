import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Webconverter.settings")
django.setup()
from django.test import TestCase, Client


class SimpleTest(TestCase):
    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_conv_to(self):
        c = Client()
        response = c.post('/converterTo/', {'currency': 'Евро', 'money': '444', 'currency2': 'Доллар'})
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        c = Client()
        response = c.post('/', {'currency': 'Евро', 'course': '82.4'})
        self.assertEqual(response.status_code, 200)
