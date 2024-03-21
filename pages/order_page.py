import allure
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators
from locators.headers_locators import HeadersLocators
from pages.base_page import BasePage
from data import TestData, Urls

class OrderPage(BasePage):
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Click order button")
    def click_order_button_up(self):
        self.driver.find_element(*HeadersLocators.BUTTON_ORDER_UP).click()

    @allure.step("Click order button")
    def click_order_button_down(self):
        try:
            self.driver.find_element(*MainPageLocators.BUTTON_ORDER_DOWN_BIG).click()
        except NoSuchElementException:
            self.driver.find_element(*MainPageLocators.BUTTON_ORDER_DOWN_MIDDLE).click()

    @allure.step("Enter name")
    def input_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step("Enter last name")
    def input_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.INPUT_LAST_NAME).send_keys(last_name)

    @allure.step("Enter address")
    def input_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step("Enter phone number")
    def input_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)

    @allure.step("Click next button")
    def click_next_button(self):
         self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    @allure.step("When to bring the scooter")
    def input_date(self, date):
        date_input = self.driver.find_element(*OrderPageLocators.INPUT_DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("The rental period")
    def select_time_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_1).click()

    @allure.step("The rental period")
    def select_time_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_2).click()

    @allure.step("Select scooter color")
    def select_scooter_color_1(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_1).click()

    @allure.step("Select scooter color")
    def select_scooter_color_2(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_2).click()

    @allure.step("Enter comment")
    def input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_SUBMIT).click()

    @allure.step("Click yes button")
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()

    @allure.step("Select metro station")
    def select_metro_station_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_1).click()

    @allure.step("Select metro station")
    def select_metro_station_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_2).click()

    @allure.step("Verify order success message")
    def is_order_confirmed(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.TEXT_ORDER_CONFIRMED))

    @allure.step("Click Yandex logo")
    def click_yandex_button(self):
        # Сохраняем текущее окно
        main_window_handle = self.driver.current_window_handle

        yandex_logo = self.driver.find_element(*HeadersLocators.YANDEX_LOGO)
        yandex_logo.click()

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != main_window_handle:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(EC.title_contains(TestData.DZEN_LOGO))

        WebDriverWait(self.driver, 10).until(EC.url_contains(TestData.DZEN_URL_REDIRECT))

    @allure.step("Click Samokat logo")
    def click_samocat_button(self):
        self.driver.find_element(*HeadersLocators.SAMOKAT_LOGO).click()
