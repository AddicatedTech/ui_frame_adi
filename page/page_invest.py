'''用来封装投资功能页面的共有操作'''


from selenium.webdriver.remote.webdriver import WebDriver
from locator.invest_locator import InvestLocator as loc
from page.base_page import BasePage
import time
class InvestPage(BasePage):
	'''思考需要封装的内容以及流程需要'''
	def get_user_amount(self):
		# 获取用户投资前的余额
		return self.get_ele_attr(loc.invest_amount_ele,"投资_获取投资前用户的金额",'data-amount')
		# return self.driver.find_element(*loc.invest_amount_ele).get_attribute('data-amount')

	def input_inv_money(self,money):
		# 输入金额
		# 先清空，之后方便下个用例载入，po模式调试自动化多在page模块进行调节
		self.driver.find_element(*loc.invest_amount_ele).clear()
		self.input_text(loc.invest_amount_ele,money,'投资_输入投资金额')

	def click_inv_btn(self):
	# 点击投资按钮
	# 	self.driver.find_element(*loc.invest_btn_ele).click()
		self.click_ele(loc.invest_btn_ele,'投资_点击投资按钮')

	def get_invest_info(self):
		# 获取投资成功信息
		ele =self.wait_ele_visibility(loc.invest_success,'投资_获取成功信息')
		# 内部自行封装的等待方法返回的是元素，然后通过元素取到需要的text属性
		return ele.text
		# return self.driver.find_element(*loc.invest_success).text


	def click_invest_success(self):
		# 点击投资成功更多信息
		# self.driver.find_element(*loc.click_success_info).click()
		ele = self.wait_ele_visibility(loc.click_success_info,'投资_点击投资成功更多信息')
		return ele.text

	def get_btn_error_info(self):
		# 获取到按钮上的提示信息
		time.sleep(0.5)
		return	self.get_ele_text(loc.invest_btn_ele,'投资_获取到按钮上的错误提示信息')
		# return self.driver.find_element(*loc.invest_btn_ele).text

	def get_alert_error_info(self):
		# 获取弹框的错误提示信息
		ele	=self.wait_ele_visibility(loc.invest_error_info,'投资_获取弹框上的错误提示信息')
		return ele.text
		# return  self.driver.find_element(*loc.invest_error_info).text


	def page_refresh(self):
		"""刷新页面"""
		self.driver.refresh()

	def click_close_error_popup(self):
		# self.driver.find_element(*loc.close_popup_btn).click()
		time.sleep(0.5)
		self.click_ele(loc.close_popup_btn,'投资_关闭错误弹框')