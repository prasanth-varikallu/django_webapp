from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_resolves_homepage(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_homepage_return_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
	    response = self.client.post('/', data={'item_text': 'A new list item'})
	    self.assertIn('A new list item', response.content.decode())
	    self.assertTemplateUsed(response, 'home.html')