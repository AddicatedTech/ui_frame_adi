# 存放 index页面相关的一系列定位信息

from selenium.webdriver.common.by import By

class IndexLocator:
### 只要是index页面中的元素定位统统放在这里

# 用户信息
	user_info = (By.XPATH,"//a[contains(text(),'我的帐户')]")
# 退出登录的按钮
	quit_btn = (By.XPATH,"//a[text()='退出']")
# 抢投标的按钮
	bid_btn_ele = (By.XPATH, "(//a[text()='抢投标'])[1]")
