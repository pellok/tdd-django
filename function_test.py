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

        #讓他可以加入另外一個項目
        #她輸入"使用孔雀羽毛來製作一隻蒼蠅"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)


        #在次更新網頁，現在他的清單有這兩個項目
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])


        # import time
        # time.sleep(10)
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
