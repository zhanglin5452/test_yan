#这是一号店的首页
import unittest
from selenium import webdriver

class FirstPage:
    def __init__(self,driver):
        self.driver=driver

    #输入10086的方法
    def input_10086(self):
        self.driver.find_element_by_id('keyword').send_keys('10086')
    #点击
    def click_keyword(self):
        self.driver.find_element_by_xpath('//*[@id="hdSearchForm"]/div/div[1]/button/i').click()
