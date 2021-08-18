# coding:utf-8
from base.base import BasePage
from selenium import webdriver
from pymouse import PyMouse
# from pynput.mouse import Controller
from pykeyboard import PyKeyboard
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
import pyautogui

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(8)

driver.get("https://oatest.guojingold.com/default/org.gocom.components.coframe.auth.login.login.flow")  # 打开百度

driver.find_element_by_xpath('//*[@id="userId$text"]').send_keys('009410')  # 定位
driver.find_element_by_xpath('//*[@id="password$text"]').send_keys('000000')  # 定位
driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div').click()  # 定位

a=driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[3]").location
# print(a)


name=driver.name
print(name)
