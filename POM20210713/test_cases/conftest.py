from py._xmlgen import html
import pytest


# 修改Environment
def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "BPM主流程自动化测试v1.0"
    config._metadata['登录地址'] = 'https://oatest.guojingold.com/default/coframe/auth/login/loginFront.jsp'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


# 修改Summary
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 国金黄金-测试中心")])
    prefix.extend([html.p("测试人员: 黄琴")])


# 删除Links
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.pop(-1)  # 删除link列


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.pop(-1)  # 删除link列
