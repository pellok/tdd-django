import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_tod_list(self):

        self.browser.get('http://localhost:8000')
        self.assertIn('To-do' ,self.browser.title) 
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
