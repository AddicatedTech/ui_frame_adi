
''''''
'''
先进行过程化编程吧用例编写出来
'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.page_login import LoginPage
from page.page_index import IndexPage
from data.case_data import LoginCase
from common.handle_logging import log
'''
执行登录操作之前要进行的操作进行
用例方法前置封装----封装至conftest
'''
@pytest.fixture(scope='class')
def pre_method():
	log.info("----------开始执行登录的用例--------")
	driver = webdriver.Chrome()
	login_page=LoginPage(driver)
	index_page=IndexPage(driver)
	yield  login_page,index_page
	driver.quit()
	log.info("-----------登录的用例执行完毕---------")


class TestLogin:

	'''思考使用pytest去编写前置方法'''
	'''
	思考用例设计场景，通过，与报错两种情况
	# 进行参数化，解包传参
'''
	@pytest.mark.skip
	@pytest.mark.parametrize('case',LoginCase.success_case_data)
	def test_login_pass(self,pre_method,case):
		# 开始执行用例 拿到前置操作返回的page对象
		login_page,index_page=pre_method
		# 取消勾选记住手机号码
		login_page.cancle_rember_mobile()
		# 调用PO对象已经封装好的方法
		login_page.login(case['mobile'], case['pwd'])
		# 进行断言
		res = index_page.get_my_user_info()
		try:
			assert '登录成功'== res
		except AssertionError as e:
			log.error(F'-------用例执行失败---case为：{case}--------')
			log.exception(e)
			raise e
		else:
			log.info("---------用例执行通过--------")
			# 退出登录。重新访问登录页面
			index_page.click_quit()
			# 重新进入登录页面
			login_page.page_refresh()

	@pytest.mark.skip
	@pytest.mark.parametrize('case',LoginCase.error_case_data)
	def test_login_error(self,pre_method,case):
		'''异常用例，窗口上会有提示'''
		login_page,index_page =pre_method
		# 刷新页面提高用例执行效率
		login_page.page_refresh()

		login_page.login(case['mobile'], case['pwd'])
		res = login_page.get_error_info()
		try:
			assert case['expected'] == res
		except AssertionError as e:
			log.error(F'-------用例执行失败---case为：{case}--------')
			log.exception(e)
			raise e
		else:
			log.info("---------用例执行通过--------")
	@pytest.mark.skip
	@pytest.mark.parametrize('case',LoginCase.error_alert_data)
	def test_login_error_alert(self,pre_method,case):
		'''异常用例，错误信息弹框提示'''
		login_page,index_page = pre_method
		# 刷新一次页面，提高用例执行效率
		login_page.page_refresh()
		login_page.login(case['mobile'],case['pwd'])
		print(case)

		res = login_page.get_alert_error_info()
		try:
			assert case['expected'] == res
		except AssertionError as e:
			log.error(F'-------用例执行失败---case为：{case}--------')
			log.exception(e)
			raise e
		else:
			log.info("---------用例执行通过--------")