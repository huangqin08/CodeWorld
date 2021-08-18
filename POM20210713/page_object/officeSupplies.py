'''
办公用品领用
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base import BasePage
from page_object.login_page import LoginPage


class OfficeSupplies(BasePage):
    url = 'https://oatest.guojingold.com/default/com.guojingold.bpm.officeSuppliesApl.Main.flow?_eosFlowAction=insert'
    # 页面元素
    # 增加按钮
    add = (By.XPATH, '//*[@id="data_form"]/div[2]/div[2]/table/tbody/tr/td[2]/a')
    frameid = "layui-layer-iframe100001"
    itemname = (By.ID, "itemname")
    confirmid = (By.ID, "confirm")
    sreach = (By.ID, "itemname")
    killIframe = (By.ID, "killIframe")
    button = (By.XPATH, "//*[@id='data_form']/table/tbody/tr[2]/td/input[2]")

    # 元素的操作流
    def office_supplies(self, sreachstr):
        # 访问url
        self.open(self.url)
        self.enter_(self.add)

        self.frame_(self.frameid)
        # 输入搜索办公
        self.input_(self.sreach, sreachstr)

        time.sleep(3)

        # 等待页面事件补全即等待下拉菜单成功展现后获取当前itemname输入框并加载键盘按下操作选中下拉菜单中的某一项
        self.down_(self.itemname)
        self.enter_(self.itemname)

        # 数据选成功后点击添加完成按钮
        self.enter_(self.confirmid)

        # 完成添加后点击关闭按钮来关闭办公用品录入界面
        self.enter_(self.killIframe)

        # 由于iframe窗口被关闭，需要把焦点事件切换到原窗口中，此时使用switch_to方法中的defaultContent来切换到原窗口位置
        self.toframe_()

        # 在原窗口中找到提交申请按钮并点击来完成流程提交
        self.enter_(self.button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    user = '009410'
    pwd = '000000'
    lp = LoginPage(driver)
    lp.login(user, pwd)
    sreachstr = '笔'
    ospage = OfficeSupplies(driver)
    ospage.office_supplies(sreachstr)
