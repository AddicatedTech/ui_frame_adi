# 封装登录之后用户页面
from selenium.webdriver.remote.webdriver import WebDriver
from locator.user_locator import UserLocator as loc
from page.base_page import BasePage
class UserPage(BasePage):

	# 获取用户余额
	def get_user_amount(self):
		amount = self.get_ele_text(loc.user_amount_ele, '用户页面_获取余额')
		amount = amount.replace('元', '')
		return amount
