import pytest
from selenium import webdriver


@pytest.fixture()
def getDriver_main_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()


@pytest.fixture()
def getDriver_register_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver
    driver.quit()


@pytest.fixture()
def getDriver_forgot_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    yield driver
    driver.quit()
