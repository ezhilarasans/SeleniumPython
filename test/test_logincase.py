import pytest

from Pages.Login_Page import LoginPage
from conftest import BaseUrl

@pytest.mark.usefixtures("browser_setup")
class Test_login:
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page=LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login("standard_user","secret_sauce")

    def teardown_class(self):
        self.driver.quit()