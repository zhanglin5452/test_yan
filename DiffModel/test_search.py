# 搜索的case
import  unittest
from selenium import webdriver
from page.first_page import FirstPage
from page.send_page import SendPage

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.yhd.com/')
        self.driver.implicitly_wait(10)
        #创建firstpage的对象
        self.firstPage=FirstPage(self.driver)
        #新建对象时 会去调用当前类的 init方法
        #创建sendpage的对象
        self.sendPage=SendPage(self.driver)
    def tearDown(self):
        self.driver.quit()
    def test_search(self):
        #PO模式就是页面和对象分离 page:页面
        #规律就是每一个页面的方法放到单独的页面中去。

        #一号店的首页
        # self.driver.find_element_by_id('keyword').send_keys('10086')
        self.firstPage.input_10086()
        # 一号店的首页
        # self.driver.find_element_by_xpath('//*[@id="hdSearchForm"]/div/div[1]/button/i').click()
        self.firstPage.click_keyword()
        try:
            #一号店的第二个页面
            # self.driver.find_element_by_xpath('//*[text()='"10086"']')
            self.sendPage.getElemnt()
            assert True
        except Exception:
            assert False