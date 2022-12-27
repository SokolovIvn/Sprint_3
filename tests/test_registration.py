from Locators import FIELD_NAME, FIELD_EMAIL, FIELD_PASSWORD, BUTTON_REGISTRATION, INFORMER_PSWD_ERROR, H2_ENTER
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import user_data

name = user_data.generate_name()
new_email = name + "@ya.ru"
bad_password = "12345"
password = user_data.generate_password()


def test_registration_bad_pswd_check_fail_text_done(getDriver_register_page):
    driver = getDriver_register_page

    field_name = driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    field_email = driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input")
    field_pswd = driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable(field_name))

    field_name.send_keys(name)
    field_email.send_keys(new_email)
    field_pswd.send_keys(bad_password)
    driver.find_element(By.XPATH, BUTTON_REGISTRATION).click()

    # Ждем когда появится форма Авторизации
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, INFORMER_PSWD_ERROR)))

    assert "Некорректный пароль" == driver.find_element(By.CSS_SELECTOR, INFORMER_PSWD_ERROR).text


def test_geristration_full(getDriver_register_page):
    driver = getDriver_register_page

    field_name = driver.find_element(By.XPATH, FIELD_NAME)
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_pswd = driver.find_element(By.XPATH, FIELD_PASSWORD)

    # Ждем когда поле ввода станет активным для ввода
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable(field_name))

    # заполняем поля для регистрации
    field_name.send_keys(name)
    field_email.send_keys(new_email)
    field_pswd.send_keys(password)
    driver.find_element(By.XPATH, BUTTON_REGISTRATION).click()

    # Ждем когда появится форма Авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, H2_ENTER)))
    assert "https://stellarburgers.nomoreparties.site/login" == driver.current_url

