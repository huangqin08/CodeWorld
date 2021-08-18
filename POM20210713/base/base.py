from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from logs.logtest import loggingtest

log1=loggingtest()

class BasePage:
    def __init__(self,driver):
        log1.info('浏览器正常启动了')
        self.driver=driver

    def open(self,url):
        log1.info('正常启动了{}'.format(url))
        # / 将Html地址get到selenium驱动打开的浏览器中并且打开这个地址
        self.driver.get(self.url)

    def locator(self,loc):
        return self.driver.find_element(*loc)

    #send_keys用于模拟用户的键盘输入
    def input_(self,loc,txt):
        log1.info('打开了{}元素，输入{}字符'.format(loc,txt))
        self.locator(loc).send_keys(txt)

    #使用click方法用于模拟用户的鼠标点击事件
    def click_(self,loc):
        self.locator(loc).click()

    # clear用于清除文本框
    def clear_(self,loc):
        self.locator(loc).clear()

    #获取该元素的文本值
    def text_(self,loc):
        textstr=self.locator(loc).text
        return textstr

    #模拟键盘ENTER键来输入
    def enter_(self,loc):
        self.locator(loc).send_keys(Keys.ENTER)

    def down_(self,loc):
        self.locator(loc).send_keys(Keys.DOWN)

    #界面是由于iframe进行嵌套，所以使用switchTo方法切换到新打开的iframe页面中，新iframe页面id在元素中自己查找
    def frame_(self,id):
        self.driver.switch_to.frame(id)

    #切换到主页面
    def toframe_(self):
        self.driver.switch_to_default_content()

    def quit(self):
        self.driver.quit()

    #直接调用javascript代码
    def script_(self,methodname):
        self.driver.execute_script(methodname)

    #鼠标滚动到页面底部
    def rool_(self):
        # for i in range(5):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        ActionChains(self.driver).key_down(Keys.DOWN).perform()
        time.sleep(5)
