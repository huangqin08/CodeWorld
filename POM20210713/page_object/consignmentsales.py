'''
费用报销流程
'''
import time
import pyautogui
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base import BasePage
from page_object.login_page import LoginPage


class ConsignmentSales(BasePage):
    url = 'https://oatest.guojingold.com/default/com.guojingold.bpm.networkreimbursement.applyCost.MainDP.flow?_eosFlowAction=insert'
    # 页面元素
    # 发票张数
    mainreq_numbercount = (By.NAME, 'mainreq/numbercount')
    # 报销事由
    mainreq_reqfuture1 = (By.NAME, 'mainreq/reqfuture1')

    # 添加按钮操作，使用注入js代码直接调用的形式
    add = "tablecontrol.addRow('grid_1')"

    # 费用承担部门
    costorgname = ("costcenter.organizationOpen(2,this)")
    frameid = 'layui-layer-iframe100001'

    # 金额
    cost = (By.XPATH, '//*[@id="7$cell$9"]/div')

    # 提交按钮
    button = 'pasRecordInsert()'

    # 元素的操作流
    def Consignment(self, numbercount, reqfuture1):
        # 访问url
        self.open(self.url)
        self.input_(self.mainreq_numbercount, numbercount)
        self.input_(self.mainreq_reqfuture1, reqfuture1)
        self.script_(self.add)
        time.sleep(3)

        # 费用科目添加
        m = PyMouse()
        k = PyKeyboard()
        k.press_key(k.page_down_key)
        time.sleep(2)
        m.click(305, 495, 1, 3)
        time.sleep(2)
        k.press_key(k.enter_key)
        k.release_key(k.enter_key)
        time.sleep(1)
        m.click(304, 494)
        time.sleep(1)
        m.click(215, 700)
        time.sleep(3)

        # 费用承担部门添加
        k.press_key(k.enter_key)
        k.release_key(k.enter_key)
        time.sleep(2)
        m.move(542, 392)
        pyautogui.click()
        pyautogui.doubleClick()

        # 金额添加
        time.sleep(2)
        pyautogui.moveTo(802, 478)
        pyautogui.rightClick()
        pyautogui.click()
        k.type_string('100')
        k.press_key(k.enter_key)
        time.sleep(2)
        # 提交按钮
        self.script_(self.button)
        time.sleep(2)

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     user = '009410'
#     pwd = '000000'
#     lp = LoginPage(driver)
#     lp.login(user, pwd)
#
#     numbercount = '1'  # 发票张数
#     reqfuture1 = '出差报销差旅费用'  # 费用事由
#     lp = ConsignmentSales(driver)
#     title = lp.Consignment(numbercount, reqfuture1)
#     print(title)
