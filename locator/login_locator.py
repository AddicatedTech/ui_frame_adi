

### 用来封装login页面所使用d到的元素定位

from selenium.webdriver.common.by import By
class LoginLocator:
	# 手机号输入框
	mobile_loc = (By.XPATH,'//input[@placeholder="手机号"]')
	# 密码输入框
	pwd_loc = (By.XPATH,'//input[@placeholder="密码"]')
	# 登录按钮
	login_btn = (By.XPATH,"//button[text()='登录']")
	# 错误提示信息
	err_hint = (By.XPATH,"//div[@class='form-error-info']")
	# 错误弹框信息
	err_alert = (By.XPATH,'//div[@class="layui-layer-content"]')

	# 记住手机号勾选框
	re_mobile = (By.XPATH,"//input[@name='remember_me']")