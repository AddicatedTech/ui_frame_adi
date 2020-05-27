from selenium.webdriver.common.by import By
from locator.index_locator import IndexLocator as loc
# 导入自己封装好的locator作为loc方便后续调入f
from page.base_page import BasePage
class IndexPage(BasePage):
    """首页"""


    def get_my_user_info(self):
        """获取我的账户信息"""
        try:
            # 此处直接调用basepage中封装好的方法，locator直接以元祖形式传入，在basepage中的方法中进行拆包
            # 1参，定位信息，2参，给截图赋的用例相关信息
            self.get_ele(loc.user_info,'首页_定位我的账户信息')
        except:
            return '登录失败'
        else:
            return '登录成功'

    def click_quit(self):
        '''点击退出登录'''
        self.click_ele(loc.quit_btn,"首页_点击退出登录")
    def click_invest_btn(self):
        # 点击抢投标的按钮
        self.click_ele(loc.bid_btn_ele,'首页_点击抢投标')