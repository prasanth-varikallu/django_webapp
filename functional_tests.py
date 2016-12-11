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

		inputbox = self.browser.find_element_by_id('uname_id')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter username')

		inputbox.send_keys('Luke')
		inputbox.send_keys(Keys.ENTER)
		self.check_row_in_list_table('1: Luke')
		self.check_row_in_list_table('2: Kylo')

		self.fail('Finished')



if __name__ == '__main__':
	unittest.main(warnings='ignore')