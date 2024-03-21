from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_time = True
        self.accept_cookies_if_first_time()

    def accept_cookies_if_first_time(self):
        if self.first_time:

            try:
                cookies_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MAIN_PAGE_COOKIE_BUTTON))
                cookies_button.click()
            except:
                pass
            self.first_time = False

    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.scroll_into_view(element)
            element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Другие общие методы
