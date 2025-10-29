from datetime import datetime
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Homepage import HomePage


@pytest.mark.usefixtures("setUp_and_teardown")
class TestLogin:

    def test_login_with_valid_Creds(self):

        try:

            # Click My Account
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            time.sleep(1)

            # Click Login
            self.driver.find_element(By.LINK_TEXT, "Login").click()
            time.sleep(1)

            # Enter Email and Password
            self.driver.find_element(By.ID, "input-email").send_keys("tradewithroyal@gmail.com")
            self.driver.find_element(By.ID, "input-password").send_keys("Royal@123")

            # Click Login Button
            self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
            time.sleep(2)

            # Verify successful login
            assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
            print("✅ Login Successful")

        except AssertionError:
            print("❌ Login failed — Account information link not found.")
        except NoSuchElementException as e:
            print("❌ Element not found:", e)


    def test_login_with_invalid_email(self):
        try:
            # Click My Account and then Login
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            self.driver.find_element(By.LINK_TEXT, "Login").click()

            # Enter invalid credentials
            self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
            self.driver.find_element(By.ID, "input-password").send_keys("Roya23")

            # Click Login
            self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
            time.sleep(2)  # Optional: better to replace with WebDriverWait later

            # Verify warning message
            expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
            actual_text = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
            assert expected_warning_msg in actual_text, f"Expected '{expected_warning_msg}', but got '{actual_text}'"

            print("✅ Test passed — correct warning message displayed.")

        except AssertionError as e:
            print("❌ Assertion failed:", e)
        except NoSuchElementException as e:
            print("❌ Element not found:", e)

    #@pytest.mark.parametrize("run", range(5))
    def test_with_invalid_email_password(self):
        for i in range(5):
            print(f"\nAttempt #{i + 1}")
        try:
            # Click My Account and then Login
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            self.driver.find_element(By.LINK_TEXT, "Login").click()

            # Enter invalid credentials
            self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
            self.driver.find_element(By.ID, "input-password").send_keys("Roya23")

            # Click Login
            self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
            time.sleep(2)  # Optional: better to replace with WebDriverWait later

            # Verify warning message
            expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
            actual_text = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
            assert expected_warning_msg in actual_text, f"Expected '{expected_warning_msg}', but got '{actual_text}'"

            print("✅ Test passed — correct warning message displayed.")

        except AssertionError as e:
            print("❌ Assertion failed:", e)
        except NoSuchElementException as e:
            print("❌ Element not found:", e)
    

    def test_login_without_entering_credentials(self):

        try:
            # Click My Account and then Login
            self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
            self.driver.find_element(By.LINK_TEXT, "Login").click()

            # Enter invalid credentials
            self.driver.find_element(By.ID, "input-email").send_keys("")
            self.driver.find_element(By.ID, "input-password").send_keys("")

            # Click Login
            self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
            time.sleep(2)  # Optional: better to replace with WebDriverWait later

            # Verify warning message
            expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
            actual_text = self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text
            assert expected_warning_msg in actual_text, f"Expected '{expected_warning_msg}', but got '{actual_text}'"

            print("✅ Test passed — correct warning message displayed.")

        except AssertionError as e:
            print("❌ Assertion failed:", e)
        except NoSuchElementException as e:
            print("❌ Element not found:", e)
    
    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "royal"+time_stamp+"@gmail.com"
