import pytest

from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=102)
class TestMisLogin:
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.mis_login_proxy = MisLoginProxy()

    def setup_method(self):
        self.driver.get("http://ttmis.research.itcast.cn/")

    def test_mis_login(self):
        username = "testid"
        password = "testpwd123"
        self.mis_login_proxy.test_mp_login(username, password)
        assert is_element_exist(self.driver, "退出")

    def teardown_class(self):
        DriverUtils.quit_mis_driver()
