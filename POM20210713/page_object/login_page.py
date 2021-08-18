'''
登录
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import BasePage


class LoginPage(BasePage):
    # 访问url
    url = 'https://oatest.guojingold.com/default/coframe/auth/login/loginFront.jsp'
    # 页面元素，地址打开
    # 使用By.id或By.NAME的方式获取页面元素id或name的值来定位该页面元素
    # 使用By.className的方式获取页面div元素的class样式值来定位数据
    # 使用By.XPATH的方式获取页面元素
    user = (By.NAME, 'userId')
    pwd = (By.NAME, 'password')
    button = (By.XPATH, '//*[@id="form1"]/div[3]/div')

    # text方法来获取该元素的文本值
    error = (By.XPATH, "//*[@id='error']")

    logout = (By.XPATH, '/html/body/div[1]/div/div/ul/li[1]/a')

    # print(error)

    # 元素的操作流
    def login(self, username, password):
        # 访问url
        self.open(self.url)
        self.input_(self.user, username)
        self.input_(self.pwd, password)
        self.click_(self.button)
        # textstr=self.text_(self.error)
        # if (textstr.find("密码错误") != -1):  #用find()或者index()两种方法都可以
        #     self.clear_(self.user)
        #     self.input_(self.user, "009410")
        #     self.clear_(self.pwd)
        #     self.input_(self.pwd, "000000")
        #     self.click_(self.button)

    # def logout(self):
    #     self.click_(self.logout)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.maximize_window()
    user='009410'
    pwd='000000'
    lp=LoginPage(driver)
    lp.login(user,pwd)
    # lp.logout()
