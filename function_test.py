import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 他馬上受邀輸入一個待辦事項
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # 他在文字方塊輸入"購買孔雀羽毛"
        # (Edith的興趣事綁蒼蠅魚餌)
        inputbox.send_keys('Buy peacock feathers')

        # 當他按下Enter時，網頁會更新，現在網頁列出
        # "1：購買孔雀羽毛" 一個待辦事項清單項目
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
            )

        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
