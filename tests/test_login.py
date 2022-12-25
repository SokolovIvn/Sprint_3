from Locators import BUTTON_ORDER, BUTTON_MAIN_ENTER, FIELD_EMAIL, FIELD_PASSWORD, BUTTON_ENTER, BUTTON_ENTER_LK, \
    BUTTON_ENTER_ON_FORM_REGISTR
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import user_data

email = user_data.get_fixture_email()
password = user_data.get_fixture_pswd()


def test_login_with_button_through_on_main(getDriver_main_page):
    driver = getDriver_main_page

    driver.find_element(By.XPATH, BUTTON_MAIN_ENTER).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    assert len(driver.find_elements(By.XPATH, BUTTON_ORDER)) == 1

    driver.quit()


def test_login_through_button_header(getDriver_main_page):
    driver = getDriver_main_page

    driver.find_element(By.XPATH, BUTTON_ENTER_LK).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    assert len(driver.find_elements(By.XPATH, BUTTON_ORDER)) == 1


def test_login_through_button_on_register_page(getDriver_register_page):
    driver = getDriver_register_page

    driver.find_element(By.XPATH, BUTTON_ENTER_ON_FORM_REGISTR).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    assert len(driver.find_elements(By.XPATH, BUTTON_ORDER)) == 1


def test_login_through_button_on_page_forgot_password(getDriver_forgot_page):
    driver = getDriver_forgot_page

    driver.find_element(By.XPATH, BUTTON_ENTER_ON_FORM_REGISTR).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    assert len(driver.find_elements(By.XPATH, BUTTON_ORDER)) == 1
