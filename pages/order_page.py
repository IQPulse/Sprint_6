from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.headers_locators import HeadersLocators
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from data import TestData

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Другие инициализации класса MainPage

    def open_page(self, url):
        self.driver.get(url)

    def click_order_button_up(self):
        self.driver.find_element(*HeadersLocators.BUTTON_ORDER_UP).click()

    def click_order_button_down(self):
        #self.driver.find_element(*MainPageLocators.BUTTON_ORDER_DOWN).click()

        try:
            button1 = self.driver.find_element(*MainPageLocators.BUTTON_ORDER_DOWN_BIG).click()

        except NoSuchElementException:
            button2 = self.driver.find_element(*MainPageLocators.BUTTON_ORDER_DOWN_MIDDLE).click()

    def input_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    def input_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.INPUT_LAST_NAME).send_keys(last_name)

    def input_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    def input_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)

    def select_metro_station_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_1).click()

    def select_metro_station_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_2).click()

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    def input_date(self, date):
        date_input = self.driver.find_element(*OrderPageLocators.INPUT_DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    def select_time_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_1).click()

    def select_time_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_2).click()

    def select_scooter_color_1(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_1).click()

    def select_scooter_color_2(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_2).click()

    def input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    def click_submit_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_SUBMIT).click()

    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()

    def is_order_confirmed(self):
         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.TEXT_ORDER_CONFIRMED))

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

    def click_samocat_button(self):
        self.driver.find_element(*HeadersLocators.SAMOKAT_LOGO).click()
