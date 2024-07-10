from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_tab = (By.XPATH, "//span[text()='PIM']")
        self.add_button = (By.XPATH, "//button[text()='Add']")
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.success_message = (By.XPATH, "//div[@class='oxd-toast-content oxd-toast-content--success']")
        self.edit_button = (By.XPATH, "//button[text()='Edit']")
        self.delete_button = (By.XPATH, "//button[text()='Delete']")
        self.confirm_delete_button = (By.XPATH, "//button[text()='Yes, Delete']")

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.pim_tab)).click()

    def click_add(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_button)).click()

    def enter_employee_details(self, first_name, last_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_field)).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.last_name_field)).send_keys(last_name)

    def click_save(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button)).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message)).text

    def edit_employee(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.edit_button)).click()

    def delete_employee(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.delete_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_delete_button)).click()
