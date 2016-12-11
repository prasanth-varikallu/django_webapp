from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import User

class HomePageTest(TestCase):

	def test_root_resolves_homepage(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_homepage_return_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
	    response = self.client.post('/', data={'username': 'Luke'})
	    self.assertIn('Luke', response.content.decode())
	    self.assertTemplateUsed(response, 'home.html')

class UserModelTest(TestCase):
	def test_saving_retrieving_usernames(self):
		first_user = User()
		first_user.username = 'Luke'
		first_user.save()

		second_user = User()
		second_user.username = 'Kylo'
		second_user.save()

		saved_users = User.objects.all()
		self.assertEqual(saved_users.count(), 2)

		first_saved_user = saved_users[0]
		second_saved_user = saved_users[1]
		self.assertEqual(first_saved_user.username, 'Luke')
		self.assertEqual(second_saved_user.username, 'Kylo')