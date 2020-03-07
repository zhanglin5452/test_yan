#这是一号店的第二个页面 也就是搜索页

class SendPage:
    def __init__(self,driver):
        self.driver=driver

    def getElemnt(self):
        self.driver.find_element_by_xpath('//*[text()='"10086"']')
