
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from unittest import skip
import sys

# Static files testing
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(8)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_tab')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])


class NewVisitorTest(FunctionalTest):

	def test_can_start_a_list_and_retrieve_it_later(self):

		# Edith has heard about a coll new online todo app. She goes
		# to check out its homepage
		# self.browser.get('http://localhost:8000')
		self.browser.get(self.server_url)

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 'Enter a to-do item'
		)

		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is trying fly-fishing lures )
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates, and now the page lists
		# "1 : Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/todolists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# There is still a text box inviting her to add another item.
		# She enters "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# (Edith is very methodical)

		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# Now a new user, Francis, comes along to the site

		# We use a new browser session to make sure that no information
		# of Edith's is coming through from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# Francis visits the home page. There is no sign of Edith's list
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text

		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# Francis starts a new list by entering a new item. He
		# is less interesting thanEdith ...
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# Francis gets his own unique url
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/todolists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# Again, there is no trace od Edith's list
		page_text = self.browser

		# Satisfied, she goes back to sleep


class LayoutAndStylingTest(FunctionalTest):

	def test_layout_and_styling(self):

		# Edith goes to the home page
		self.browser.get(self.server_url)
		self.browser.set_window_size(741, 390)

		# She notices the input box is nicely centered
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2, 370.5, delta=5
		)

		# She starts a new list and sees the input is nicely
		# centered there too
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2, 370.5, delta=5
		)


class ItemValidationTest(FunctionalTest):

	@skip
	def test_cannot_add_empty_list_items(self):

		# Edith goes to the home page amd accidentally tries to submit

		# an empty list item. She hits Enter on the empty input box.
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# The home page refreshes, and there is an error message saying

		# those list items cannot be blank
		error = self.browser.find_element_by_css_selector('.has-error')

		self.assertEqual(error.text," You can't have an empty list")

		# She tries again with some test for the item, which now works

		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# Perversly she now decides to submit a second blank list item

		# She receives a similar warning on the list page

		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')


		# And she can correct it by filling some text in
		self.fail('write me!')

# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')