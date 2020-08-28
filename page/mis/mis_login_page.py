"""后台管理系统登录界面"""

# 对象库层:管理维护页面的所有元素对象
from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle
from utils import DriverUtils


class MisLoginPage(BasePage):
    # 在初始化方法定义实例属性来管理元素对象的定位方式以及对应的表达式方法
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = (By.NAME, "username")
        # 密码输入框
        self.password = (By.NAME, "password")
        # 登录按钮
        self.login_btn = (By.ID, "inp1")

    # 定义实例方法来找到具体的元素对象
    def find_username(self):
        return self.find_elt(self.username)

    def find_password(self):
        return self.find_elt(self.password)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层:专门封装元素对象的操作方法
class MisLoginHandle(BaseHandle):
    def __init__(self):
        self.mis_login_page = MisLoginPage()

    def input_username(self, username):
        self.input_text(self.mis_login_page.find_username(), username)

    def input_password(self, password):
        self.input_text(self.mis_login_page.find_password(), password)

    def click_login_btn(self):
        js_str = "document.getElementById('inp1').removeAttribute('disabled')"
        DriverUtils.get_mis_driver().execute_script(js_str)
        self.mis_login_page.find_login_btn().click()


# 业务层：连续调用多个操作层方法完成测试用例手工操作
class MisLoginProxy:
    def __init__(self):
        self.mis_login_handle = MisLoginHandle()

    def test_mp_login(self, username, password):
        self.mis_login_handle.input_username(username)
        self.mis_login_handle.input_password(password)
        self.mis_login_handle.click_login_btn()
