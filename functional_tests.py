from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class BasicTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_list_retrieve_it(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		mainDish_box = self.browser.find_element_by_id('main_dish_id')
		sideDish_box = self.browser.find_element_by_id('side_dish_id')
		self.assertEqual(mainDish_box.get_attribute('placeholder'), 'Enter main dish')
		self.assertEqual(sideDish_box.get_attribute('placeholder'), 'Enter side dish')

		mainDish_box.send_keys('Pizza')
		sideDish_box.send_keys('Chips')
		mainDish_box.send_keys(Keys.ENTER)
		sideDish_box.send_keys(Keys.ENTER)

		self.check_row_in_list_table('1: Pizza')
		self.check_row_in_list_table('1: Chips')
		self.check_row_in_list_table('2: Hoagie')
		self.check_row_in_list_table('2: Pickle')

		self.fail('Finished')



if __name__ == '__main__':
	unittest.main(warnings='ignore')