import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


# @pytest.fixture()
# def setup_and_teardown():
#     global driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get('https://tutorialsninja.com/demo/')
#     yield
#     driver.quit()

@pytest.mark.usefixtures("setUp_and_teardown")
class TestRegister:
    driver = None

    def test_register_with_mandatory_fields(self):

        try:
            # Click My Account
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            time.sleep(2)
            # Click on Register
            self.driver.find_element(By.LINK_TEXT, 'Register').click()

            # Verifying Register Page
            assert self.driver.find_element(By.XPATH, '(//h1[normalize-space()="Register Account"])[1]').is_displayed()
            print("✅ Registration Form Verification is Successful")

            # Filling out the Registration form
            self.driver.find_element(By.ID,"input-firstname").send_keys("Royal")
            self.driver.find_element(By.ID, "input-lastname").send_keys("Singh")
            self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
            self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
            self.driver.find_element(By.ID, "input-password").send_keys("12345")
            self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
            self.driver.find_element(By.NAME, "agree").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
            time.sleep(2)
            expected_heading_text = "Your Account Has Been Created!"
            assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)
            print("✅ Registration with Mandatory Field is Successful")


        except AssertionError as e:

            print("❌ Assertion failed:", e)

        except NoSuchElementException as e:

            print("❌ Element not found:", e)

    def test_Register_with_all_fields(self):

        try:
            # Click My Account
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            time.sleep(2)
            # Click on Register
            self.driver.find_element(By.LINK_TEXT, 'Register').click()

            # Verifying Register Page
            assert self.driver.find_element(By.XPATH, '(//h1[normalize-space()="Register Account"])[1]').is_displayed()
            print("✅ Registration Form Verification is Successful")

            # Filling out the Registration form
            self.driver.find_element(By.ID, "input-firstname").send_keys("Royal")
            self.driver.find_element(By.ID, "input-lastname").send_keys("Singh")
            self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
            self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
            self.driver.find_element(By.ID, "input-password").send_keys("12345")
            self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
            self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
            self.driver.find_element(By.NAME, "agree").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
            time.sleep(2)
            expected_heading_text = "Your Account Has Been Created!"
            assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)
            print("✅ Registration with All Fields is Successful")


        except AssertionError as e:

            print("❌ Assertion failed:", e)

        except NoSuchElementException as e:

            print("❌ Element not found:", e)

    def test_Register_with_duplicate_Email(self):

        try:
            # Click My Account
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            time.sleep(2)
            # Click on Register
            self.driver.find_element(By.LINK_TEXT, 'Register').click()

            # Verifying Register Page
            assert self.driver.find_element(By.XPATH, '(//h1[normalize-space()="Register Account"])[1]').is_displayed()
            print("✅ Registration Form Verification is Successful")

            # Filling out the Registration form
            self.driver.find_element(By.ID, "input-firstname").send_keys("Royal")
            self.driver.find_element(By.ID, "input-lastname").send_keys("Singh")
            self.driver.find_element(By.ID, "input-email").send_keys("jfhkhkjks@gmail.com")
            self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
            self.driver.find_element(By.ID, "input-password").send_keys("12345")
            self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
            self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
            self.driver.find_element(By.NAME, "agree").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
            time.sleep(2)
            expected_heading_text = "Warning: E-Mail Address is already registered!"
            assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__eq__(expected_heading_text)
            print("✅ Correct Warning Displayed: E-Mail Address is already registered")


        except AssertionError as e:

            print("❌ Assertion failed:", e)

        except NoSuchElementException as e:

            print("❌ Element not found:", e)


    def test_Register_with_empty_form(self):

        try:
            # Click My Account
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            time.sleep(2)
            # Click on Register
            self.driver.find_element(By.LINK_TEXT, 'Register').click()

            # Verifying Register Page
            assert self.driver.find_element(By.XPATH, '(//h1[normalize-space()="Register Account"])[1]').is_displayed()
            print("✅ Registration Form Verification is Successful")

            # Filling out the Registration form
            self.driver.find_element(By.ID, "input-firstname").send_keys("")
            self.driver.find_element(By.ID, "input-lastname").send_keys("")
            self.driver.find_element(By.ID, "input-email").send_keys("")
            self.driver.find_element(By.ID, "input-telephone").send_keys("")
            self.driver.find_element(By.ID, "input-password").send_keys("")
            self.driver.find_element(By.ID, "input-confirm").send_keys("")
            self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
            self.driver.find_element(By.NAME, "agree").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
            time.sleep(2)
            expected_firstname_warning_text = "First Name must be between 1 and 32 characters!"
            assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__contains__(expected_firstname_warning_text)
            print("✅ Correct Warning Displayed: First Name must be between 1 and 32 characters")


        except AssertionError as e:

            print("❌ Assertion failed:", e)

        except NoSuchElementException as e:

            print("❌ Element not found:", e)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "royal"+time_stamp+"@gmail.com"




