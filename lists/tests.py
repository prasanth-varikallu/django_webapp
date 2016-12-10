from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):

	def test_sample(self):
		self.assertEqual(2, 3)