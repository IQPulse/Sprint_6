from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_question_and_get_answer_text(self, locator_q, num):
        method, locator = locator_q
        locator = locator.format(num)

        element = self.find_element_with_wait((method, locator))
        self.scroll_into_view(element)

        try:
            self.click_on_element((method, locator))
        except ElementClickInterceptedException:
            self.scroll_into_view(element)
            self.click_on_element((method, locator))

        answer_locator_method, answer_locator = MainPageLocators.ANSWER_LOCATOR
        answer_locator = answer_locator.format(num)
        return self.get_text_from_element((answer_locator_method, answer_locator))
