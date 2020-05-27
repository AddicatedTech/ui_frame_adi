'''存放投资功能所涉及到的元素操作节点信息'''

from selenium.webdriver.common.by import By
class InvestLocator:
	# # 投标金额输入框定位 placeholder 属性可提取可用余额
	# invest_input =(By.XPATH,"//div[@class='clearfix left']/input")
	#
	# # 抢投标按钮定位//div[@class='pd-right']/button
	# # 输入非10的时候会显示提示信息 请输入10的整数倍
	# invest_btn =(By.XPATH,"//div[@class='pd-right']/button")
	#
	# # 参数不合规弹出提示框定位
	# inlegal_alert =(By.XPATH,"//div[@id='layui-layer1']//div[@class='text-center']")
	# # 投标成功后弹出提示框的定位
	# pass_alert=(By.XPATH,"//div[@class='layui-layer-content']//div[contains(text(),'投标成功')]")
	# 投资金额输入框 引用的地方有两个
	invest_amount_ele = (By.XPATH, "//input[@data-amount]")

	# 投资点击按钮
	invest_btn_ele = (By.XPATH, '//button[@class="btn btn-special height_style"]')

	# 投资成的提示元素
	invest_success = (By.XPATH, '//div[text()="投标成功！"]')

	# 投资成功点击查看更多的方法
	click_success_info = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')

	# 投资失败，错误弹框提示信息
	invest_error_info = (By.XPATH, '//div[@class="text-center"]')

	# 确认关闭弹框
	close_popup_btn = (By.XPATH,'//a[text()="确认"]')
