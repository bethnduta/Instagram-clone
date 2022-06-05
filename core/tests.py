from django.test import TestCase
from . models import post
from django.contrib.auth.models import User
# Create your tests here.
class PostTest(TestCase):
    def test_str(self):
        test_title = post(caption='A picture')
        self.assertEqual(str(test_title),'A picture')

    def test_instance(self):
        self.assertTrue(isinstance(post(),post))    