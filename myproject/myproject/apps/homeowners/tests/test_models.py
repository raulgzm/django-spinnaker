# Python imports
# Django imports
from django.test import TestCase
# Third-Party imports
# Apps imports
from .mocks import create_object_homeowner

class HomeOwnersModelsTestCase(TestCase):

    def setUp(self):
        self.homeowner = create_object_homeowner(
            email='hi@brainattica.com',
            password='Brainattica'
        )

    def test_str_method(self):
        self.assertIsInstance(self.homeowner.__str__(), str)
