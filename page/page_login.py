''''''
'''
思考PO模式 page里面都需要封装哪些共有的代码
 1访问到主页面
 2向目标输入框传参数,进行点击登录
 4查看登录操作回显信息
'''
from locator.login_locator import LoginLocator as loc
from common.handle_config import  conf
from selenium.webdriver.remote.webdriver import WebDriver
# 上面这个remote.webdriver是为了方便在封装page的时候可以有输入提示
from page.base_page import BasePage
class LoginPage(BasePage):
	#
	url = conf.get('url','base_url') + conf.get("url","login_url")
	def __init__(self, driver):

		super().__init__(driver)
		# 打开登录页面
		self.driver.get(self.url)
		self.driver.implicitly_wait(15)

	def login(self,user,pwd):
		'''传入用户名和密码，然后进行登录'''
		self.input_text(loc.mobile_loc,user,"登录_账号输入")
		# 输入密码
		self.input_text(loc.pwd_loc,pwd,"登录_密码输入")
		# 点击登录
		self.click_ele(loc.login_btn,"登录_点击登录按钮")

	def get_error_info(self):
		'''获取到失败的提示消息'''
		return self.get_ele_text(loc.err_hint,'登录_获取到失败的提示消息（非弹框)')

	def get_alert_error_info(self):
		"""获取页面弹窗的错误提示信息"""
		return self.get_ele_text(loc.err_alert,'登录_页面弹窗错误提示')

	def page_refresh(self):
		# 刷新页面，提高用例执行效率  操作selenium再次访问元页面
		self.driver.get(url=self.url)

	def cancle_rember_mobile(self):
		# 取消记住手机号，方便多条用例执行
		self.click_ele(loc.re_mobile,'登录_点击取消记住手机号')