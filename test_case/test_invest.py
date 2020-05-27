import time
from decimal import Decimal

import pytest
from selenium import webdriver
from page.page_login import LoginPage
from page.page_index import IndexPage
from page.page_invest import InvestPage
from page.page_user import UserPage
from common.handle_logging import log
from common.handle_config import conf
from data.case_data import InvestData


# 思考前置条件
# 先进行登录


@pytest.fixture(scope='class')
def invest_flxure():
	log.info("----------开始执行登录的用例--------")
#设置driver以无头浏览器的模式运行
	option =webdriver.ChromeOptions()
	option.add_argument("--headless")
	driver = webdriver.Chrome(options=option)
	# 创建登录页面
	# driver.maximize_window()
	driver.implicitly_wait(15)
	login_page = LoginPage(driver)
	# 登录
	login_page.login(user=conf.get('test_data', 'mobile'), pwd=conf.get('test_data', 'pwd'))
	# 创建首页对调用点击
	index_page = IndexPage(driver)
	index_page.click_invest_btn()
	# 点击之后进入投资页面
	invest_page = InvestPage(driver)
	# 需要使用到 用户页面进行用例执行
	user_page = UserPage(driver)
	yield invest_page, user_page

	driver.quit()




class TestInvest:

	@pytest.mark.parametrize('case', InvestData.error_data)
	def test_invest_error(self, case, invest_flxure):
		# 每条用例执行之前，刷新页面，解决用例连续执行的问题
		# 但是还可以进行优化，比如将输入框清空  使用js获取元素然后调用clear方法
		# 前置方法flexture返回的是一个元祖形式的数据，
		# 场景： 投资失败，按钮上出现提示的用例
		invest_page = invest_flxure[0]
		invest_page.input_inv_money(case["money"])
		# 获取按钮提示信息
		res = invest_page.get_btn_error_info()
		# 关掉弹框
		# invest_page.click_close_error_popup()
		try:
			assert case['expected'] == res
		except AssertionError as e:
			log.error(F"用例--{case['title']}---执行未通过")
			log.exception(e)
			raise e
		else:
			log.info(F"用例--{case['title']}---执行通过")

	@pytest.mark.parametrize('case', InvestData.error_popup_data)
	def test_invest_error_alert(self, case, invest_flxure):
		# 投资失败，弹框上出现提示信息的用例
		invest_page = invest_flxure[0]
		# 输入投资金额
		invest_page.input_inv_money(case['money'])
		# 点击投资
		invest_page.click_inv_btn()
		# 获取到页面弹框提示
		res = invest_page.get_alert_error_info()
		# 手动关闭弹框
		invest_page.click_close_error_popup()
		try:
			assert case['expected'] == res
		except AssertionError as e:
			log.error(F"用例--{case['title']}---执行未通过")
			log.exception(e)
			raise e
		else:
			log.info(F"用例--{case['title']}---执行通过")

	# 投资成功的案例，需要检验投资前后金额是否正常
	@pytest.mark.parametrize('case', InvestData.success_data)
	def test_invest_success(self, case, invest_flxure):
		invest_page, user_page = invest_flxure
		# 获取到用户投资之前的金额
		before_money = invest_page.get_user_amount()
		# 输入投资金额
		invest_page.input_inv_money(case['money'])
		# 点击投资
		invest_page.click_inv_btn()
		# 获取页面弹框的成功消息
		res = invest_page.get_invest_info()
		# 点击查看投资成功的信息，跳转到用户页面
		invest_page.click_invest_success()
		# 获取用户页面的余额， 投资后
		after_money = user_page.get_user_amount()
		try:
			assert case["expected"] == res
			# 因为含有小数
			assert Decimal(before_money) - Decimal(after_money) == Decimal(case['money'])
		except AssertionError as e:
			log.error(F"用例--{'投资金额为' + case['money']}---执行未通过")
			log.exception(e)
			time.sleep(10)
			raise e
		else:
			log.info(F"用例--{'投资金额为' + case['money']}---执行通过")
