import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from selenium import webdriver
from page_object.login_page import LoginPage
from page_object.officeSupplies import OfficeSupplies
from page_object.consignmentsales import ConsignmentSales
from ddt import ddt, file_data, data, unpack

from test_cases.findnewfile import find_newest_file
from test_cases.sendmessage import send_email


@ddt
class Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 加载driver驱动，使得newChromeDriver()对象能正常被调用
        # 获取chrome驱动并正确打开浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.lp = LoginPage(cls.driver)
        cls.ospage = OfficeSupplies(cls.driver)
        cls.cost = ConsignmentSales(cls.driver)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.close()
        # pass

    # @file_data('../data/testdata.yaml')
    # @data({'user': '009410', 'pwd': '000000'}, )
    @data(['009410', '000000'])
    @unpack
    def test_01(self, user, pwd):
        # print('user', user)
        # print(pwd)
        # 登录流程
        # user = '009410'
        # pwd = '000000'
        # self.lp.login(kwargs['user'], kwargs['pwd'])
        self.lp.login(user, pwd)
        title = self.driver.title
        self.assertIn(u"国金黄金首页", title, msg='断言失败')

    # @unittest.skip("跳过")
    @data('笔')
    def test_02(self, txt):
        # # 办公用品领用流程
        # sreachstr = '笔'
        # # self.ospage.office_supplies(kwargs['sreachstr'])
        self.ospage.office_supplies(txt)

    # @unittest.skip("跳过")
    def test_03(self):
        # 费用报销流程
        numbercount = '1'  # 发票张数
        reqfuture1 = '出差报销差旅费用'  # 费用事由
        self.cost.Consignment(numbercount, reqfuture1)
        title = self.driver.title
        self.assertEqual(title, u"申请记录", msg='断言失败')

    if __name__ == '__main__':
        print('=====AutoTest Start======')
        # 指定测试用例为当前文件夹下的test_case目录
        test_dir = 'C:/Users/xinxi/PycharmProjects/POM20210713/test_cases'
        # 测试报告的路径
        test_report_dir = './report'
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
        now = time.strftime('%Y-%m-%d_%H_%M_%S_')

        # 生成测报告的路径
        filename = test_report_dir + '\\' + now + 'result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

        # 运行
        runner.run(discover)
        fp.close()
        print('测试结束')

        # 查找最新的测试报告
        file_newest = find_newest_file(test_report_dir)

        # 发送最新的测试报告
        send_email(file_newest)
