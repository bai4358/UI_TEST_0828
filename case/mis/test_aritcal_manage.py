import pytest

import config
from page.mis.mis_aaritcal_page import MisAtcalProxy
from page.mis.mis_home_page import MisHomePage
from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=103)
class TestAritcalMana:
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.login_page = MisLoginProxy()
        self.home_page = MisHomePage()
        self.ad_page = MisAtcalProxy()

    def test_aduit_ari_pass(self):
        ari_titlt = config.PUB_ARITCAL_TITLE
        print("审核文章的标题为：---->",ari_titlt)
        self.home_page.to_aaritcal_page()
        self.ad_page.test_aduit_pass(ari_titlt)
        assert is_element_exist(self.driver, "驳回")

    def teardown_class(self):
        DriverUtils.quit_mis_driver()
