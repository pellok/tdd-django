import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 他去查看首頁
        self.browser.get('http://localhost:8000')
        # 發現網頁標題與標頭顯示代辦事項清單
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').header_text
        self.assertIn('To-Do', header_text)

        # 他馬上受邀輸入一個待辦事項
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
