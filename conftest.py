import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import TestData

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    driver.get(TestData.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()




