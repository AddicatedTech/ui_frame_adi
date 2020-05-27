# 首先先观察都有哪些操作可以提出来封装到总页面，之后通过继承的方式进行调用

# 显示等待  可见，可点击， 被夹在

# 元素定位错误的话log输出，
# 元素定位错误的话截图输出

# 取得元素的文本信息 text

# 进行元素点击  click

# 刷新？
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time
import os
from common.handle_logging import log
from common.handle_path import ERROR_IMG
class BasePage:

	def __init__(self,drvier:WebDriver):
		# 需要先传入一个 driver对象 用作selenium初始化
		self.driver = drvier


	def wait_ele_visibility(self,locator,img_info,timeout=15,poll_frequency=0.5):
		# 可见
		# 设置一个计时器
		st_time=time.time()
		try:
			ele =WebDriverWait(self.driver,timeout,poll_frequency).until(
				EC.visibility_of_element_located(locator))
		except Exception as e:
			log.error("元素--{}--等待可见超时".format(locator))
			log.exception(e)
			# 截图方法
			self.save_error_image(img_info)

			raise e
		else:
			end_time = time.time()
			log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - st_time))
			return ele



	def wait_ele_clickble(self,locator,img_info,timeout=15,poll_frequency=0.5):
		# 可点击
		st_time=time.time()
		try:
			ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
				EC.element_to_be_clickable(locator))
		except Exception as e:
			log.error("元素--{}--等待可点击超时".format(locator))
			log.exception(e)
			# 截图方法
			self.save_error_image(img_info)
			raise e
		else:
			end_time = time.time()
			log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - st_time))
			return ele

	def wait_ele_presence(self,locator,img_info,timeout=15,poll_frequency=0.5):
		# 被加载
		st_time=time.time()
		try:
			ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
				EC.presence_of_element_located(locator))
		except Exception as e:
			log.error("元素--{}--等待被加载超时".format(locator))
			log.exception(e)
			# 截图方法
			self.save_error_image(img_info)
			raise e
		else:
			end_time = time.time()
			log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - st_time))
			return ele

# -------------元素操作相关
	def get_ele_text(self,locator,img_info):
		# 获取元素包含text信息 需要传入loactor 还要进行拆包
		try:
			text = self.driver.find_element(*locator).text
		except Exception as e:
			# 输出日志
			log.error("元素--{}--获取文本失败".format(locator))
			log.exception(e)
			# 对当前页面进行截图
			self.save_error_image(img_info)
			raise e
		else:
			log.info("元素--{}--获取文本成功".format(locator))
			return text

	def click_ele(self,locator,img_info):
		# 点击元素
		try:
			self.driver.find_element(*locator).click()
		except Exception as e:
			# 输出日志
			log.error("元素--{}--点击元素失败".format(locator))
			log.exception(e)
			# 对当前页面进行截图
			self.save_error_image(img_info)
			raise e
		else:
			log.info("元素--{}--点击成功".format(locator))

	def input_text(self,locator,input,img_info):
		# 像元素输入内容
		try:
			self.driver.find_element(*locator).send_keys(input)
		except Exception as e:
			# 输出日志
			log.error("输入文本--{}--失败".format(locator))
			log.exception(e)
			# 对当前页面进行截图
			start_time = time.time()
			# filename = '{}_{}.png'.format(img_info, start_time)
			# file_path = os.path.join(ERROR_IMG, filename)
			self.save_error_image(img_info)
			raise e
		else:
			log.info("文本内容输入--{}--成功".format(locator))

	def get_ele(self,locator,img_info):
		# 获取到元素节点
		try:
			ele = self.driver.find_element(*locator)
		except Exception as e:
			# 输出日志
			log.error("获取元素--{}--失败".format(locator))
			log.exception(e)
			# 对当前页面进行截图   imginfo 错误截图信息由调用处传入
			self.save_error_image(img_info)
			raise e
		else:
			log.info("元素--{}--获取成功".format(locator))
			return ele

	def get_ele_attr(self,locator,img_info,attr_name):
		# 获取元素节点的属性，传入为属性名
		try:
			ele = self.driver.find_element(*locator)
			attr_value = ele.get_attribute(attr_name)
		except Exception as e:
			# 输出日志
			log.error(F"获取元素--{locator}--属性失败")
			log.exception(e)
			# 对当前页面进行截图
			self.save_error_image(img_info)
			raise e
		else:
			log.info(F"获取元素--{locator}--属性成功")
			return attr_value

	def save_error_image(self,img_info):
		# img_info 错误截图信息
		record_time =time.time() # 记录时间
		img_name=F'{img_info}_{record_time}.png' # 拼接图片名 主要包含用例执行信息，执行时间
		file_path = os.path.join(ERROR_IMG, img_name) # 拼接组成文件路径
		self.driver.save_screenshot(file_path) # 调用方法进行保存
		log.info(F"错误页面截屏成功，保存路径为{file_path}")

