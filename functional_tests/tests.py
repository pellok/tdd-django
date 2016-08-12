# encoding=utf8
from __future__ import unicode_literals
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # 他去查看首頁
        self.browser.get(self.live_server_url)
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

        # 讓他可以加入另外一個項目
        # 她輸入"使用孔雀羽毛來製作一隻蒼蠅"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 在次更新網頁，現在他的清單有這兩個項目
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # import time
        # time.sleep(10)
        self.fail('Finish the test')
