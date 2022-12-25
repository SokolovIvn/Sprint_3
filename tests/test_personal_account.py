from Locators import FIELD_EMAIL, FIELD_PASSWORD, BUTTON_MAIN_ENTER, BUTTON_ENTER, BUTTON_ORDER, BUTTON_ENTER_LK, \
    HREF_PROFILE, BUTTON_EXIT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import user_data

email = user_data.get_fixture_email()
password = user_data.get_fixture_pswd()


def test_login_go_to_lk_through_header():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, BUTTON_MAIN_ENTER).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    driver.find_element(By.XPATH, BUTTON_ENTER_LK).click()

    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, HREF_PROFILE)))

    assert "https://stellarburgers.nomoreparties.site/account/profile" in driver.current_url

    driver.quit()


def test_log_out_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, BUTTON_MAIN_ENTER).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    driver.find_element(By.XPATH, BUTTON_ENTER_LK).click()

    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_EXIT)))
    driver.find_element(By.XPATH, BUTTON_EXIT).click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//h2")))

    assert "Вход" == driver.find_element(By.XPATH, ".//h2").text

    driver.quit()
