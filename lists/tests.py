from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Food

class HomePageTest(TestCase):

	def test_homepage_return_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


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

class ListViewTest(TestCase):

	def test_use_orders_template(self,):
		response = self.client.get('/orders/first-order-ever/')
		self.assertTemplateUsed(response, 'order.html')

	def test_display_all(self,):
		Food.objects.create(main_dish='Sandwitch', side_dish='Chips')
		Food.objects.create(main_dish='Wrap', side_dish='Cookie')

		response = self.client.get('/orders/first-order-ever/')
		self.assertContains(response, 'Sandwitch')
		self.assertContains(response, 'Chips')
		self.assertContains(response, 'Wrap')
		self.assertContains(response, 'Cookie')

class NewOrderTest(TestCase):

	def test_save_POST_food(self,):
		response = self.client.post('/orders/new', data={'main_dish': 'Salad', 'side_dish': 'Soup', })
		self.assertEqual(Food.objects.count(), 1)
		new_food = Food.objects.first()
		self.assertEqual(new_food.main_dish, 'Salad')
		self.assertEqual(new_food.side_dish, 'Soup')
	
	def test_redirect_after_POST(self,):
		response = self.client.post('/orders/new', data={'main_dish': 'Salad', 'side_dish': 'Soup', })
		self.assertRedirects(response, '/orders/first-order-ever/')