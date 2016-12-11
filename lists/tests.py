from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Food

class HomePageTest(TestCase):

	def test_root_resolves_homepage(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_homepage_return_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_only_save_foods_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Food.objects.count(), 0)

	def test_display_all_foods(self):
		Food.objects.create(main_dish='Sandwitch', side_dish='Chips')
		Food.objects.create(main_dish='Wrap', side_dish='Cookie')

		response = self.client.get('/')
		self.assertIn('Sandwitch', response.content.decode())
		self.assertIn('Chips', response.content.decode())
		self.assertIn('Wrap', response.content.decode())
		self.assertIn('Cookie', response.content.decode())


class foodModelTest(TestCase):
	def test_saving_retrieving_food(self):
		first_food = Food()
		first_food.main_dish = 'Pizza'
		first_food.side_dish = 'Chips'
		first_food.save()

		second_food = Food()
		second_food.main_dish = 'Hoagie'
		second_food.side_dish = 'Pickle'
		second_food.save()

		saved_foods = Food.objects.all()
		self.assertEqual(saved_foods.count(), 2)

		first_saved_food = saved_foods[0]
		second_saved_food = saved_foods[1]
		self.assertEqual(first_saved_food.main_dish, 'Pizza')
		self.assertEqual(first_saved_food.side_dish, 'Chips')
		self.assertEqual(second_saved_food.main_dish, 'Hoagie')
		self.assertEqual(second_saved_food.side_dish, 'Pickle')

	def test_save_POST_food(self,):
		response = self.client.post('/', data={'main_dish': 'Salad', 'side_dish': 'Soup', })
		self.assertEqual(Food.objects.count(), 1)
		new_food = Food.objects.first()
		self.assertEqual(new_food.main_dish, 'Salad')
		self.assertEqual(new_food.side_dish, 'Soup')
	
	def test_redirect_after_POST(self, ):
		response = self.client.post('/', data={'main_dish': 'Salad', 'side_dish': 'Soup', })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')