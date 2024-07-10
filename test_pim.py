import pytest
from pages.login_page import LoginPage
from pages.pim_page import PIMPage


@pytest.mark.usefixtures("setup")
class TestPIM:
    def setup_method(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

    def test_add_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.navigate_to_pim()
        pim_page.click_add()
        pim_page.enter_employee_details("John", "Doe")
        pim_page.click_save()
        success_message = pim_page.get_success_message()
        assert success_message == "Successfully Saved"

    def test_edit_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.navigate_to_pim()
        pim_page.edit_employee()
        pim_page.enter_employee_details("Jane", "Smith")
        pim_page.click_save()
        success_message = pim_page.get_success_message()
        assert success_message == "Successfully Updated"

    def test_delete_employee(self):
        pim_page = PIMPage(self.driver)
        pim_page.navigate_to_pim()
        pim_page.delete_employee()
        success_message = pim_page.get_success_message()
        assert success_message == "Successfully Deleted"