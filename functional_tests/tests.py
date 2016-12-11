from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class BasicTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def identify_text_box_button(self,):
		self.mainDish_box = self.browser.find_element_by_id('main_dish_id')
		self.sideDish_box = self.browser.find_element_by_id('side_dish_id')
		self.button_box = self.browser.find_element_by_tag_name('button')

	def test_can_start_order_single_user(self,):
		self.browser.get(self.live_server_url)

		self.assertIn('NoWait', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Your Order', header_text)

		self.identify_text_box_button()
		self.assertEqual(self.mainDish_box.get_attribute('placeholder'), 'Enter main dish')
		self.assertEqual(self.sideDish_box.get_attribute('placeholder'), 'Enter side dish')
		self.mainDish_box.send_keys('Pizza')
		self.sideDish_box.send_keys('Chips')
		self.button_box.click()

		self.identify_text_box_button()
		self.mainDish_box.send_keys('Hoagie')
		self.sideDish_box.send_keys('Pickle')
		self.button_box.click()

		self.check_row_in_list_table('1: Pizza Chips')
		self.check_row_in_list_table('2: Hoagie Pickle')
		
	def test_multiple_orders_multiple_urls(self,):
		self.browser.get(self.live_server_url)

		self.identify_text_box_button()
		self.mainDish_box.send_keys('Hoagie')
		self.sideDish_box.send_keys('Pickle')
		self.button_box.click()

		self.check_row_in_list_table('1: Hoagie Pickle')
		first_order_url = self.browser.current_url
		self.assertRegex(first_order_url, '/orders/.+')

		# New order
		self.browser.quit()
		self.browser = webdriver.Firefox()

		self.browser.get(self.live_server_url)
		# Check if old orderdetails are present
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Pizza Chips', page_text)
		self.assertNotIn('Hoagie Pickle', page_text)

		# Create new order
		self.identify_text_box_button()
		self.mainDish_box.send_keys('Salad')
		self.sideDish_box.send_keys('Soup')
		self.button_box.click()

		# Assert new order url
		second_order_url = self.browser.current_url
		self.assertRegex(second_order_url, '/orders/.+')
		self.assertNotEqual(first_order_url, second_order_url)

		# Check again if old orderdetails are present
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Pizza Chips', page_text)
		self.assertNotIn('Hoagie Pickle', page_text)

if __name__ == '__main__':
	unittest.main(warnings='ignore')