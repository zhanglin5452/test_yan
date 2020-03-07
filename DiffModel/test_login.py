#登录成功和失败的case
import unittest
from selenium import webdriver
from time import sleep

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.yhd.com/')
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
    def test_login_success(self):
        self.driver.find_element_by_partial_link_text('登录').click()
        self.driver.find_element_by_id('un').send_keys('zhangqingmei1233')
        self.driver.find_element_by_id('pwd').send_keys('zhangqingmei1233')
        self.driver.find_element_by_class_name('login_btn').click()
        try:
            self.driver.find_element_by_xpath("//*[text()='zhangqingmei1233']")
            assert True
        except Exception:
            assert False
    def test_login_fail(self):
        self.driver.find_element_by_partial_link_text('登录').click()
        self.driver.find_element_by_id('un').send_keys('zhangqingmei1233')
        self.driver.find_element_by_id('pwd').send_keys('zhangqingmei1234')
        self.driver.find_element_by_class_name('login_btn').click()
        try:
            self.driver.find_element_by_xpath("//*[text()='账号和密码不匹配，请重新输入']")
            assert True
        except Exception:
            assert False
