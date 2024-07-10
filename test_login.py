import pytest
from pages.login_page.py import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_successful_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        # Verify successful login (You may need to check for a specific element that's only visible upon successful login)

    def test_invalid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("invalidpassword")
        login_page.click_login()
        error_message = login_page.get_error_message()
        assert error_message == "Invalid credentials"