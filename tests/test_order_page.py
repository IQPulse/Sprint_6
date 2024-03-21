import allure
from pages.order_page import OrderPage
from data import TestData, Urls


def perform_order_process(order_page, order_button_click, name, last_name, address, metro_station, phone, date, time_function,
                          color, comment):
    order_button_click()
    order_page.input_name(name)
    order_page.input_last_name(last_name)
    order_page.input_address(address)
    metro_station()
    order_page.input_phone(phone)
    order_page.click_next_button()
    order_page.input_date(date)
    time_function()
    color()
    order_page.input_comment(comment)
    order_page.click_submit_button()
    order_page.click_yes_button()


@allure.feature("Order Page")
@allure.story("Order Process")
class TestOrderPage:
    @allure.title("Make order one")
    @allure.severity(allure.severity_level.NORMAL)
    def test_make_order_one(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.BASE_URL)

        perform_order_process(order_page, order_page.click_order_button_up, TestData.NAME, TestData.LAST_NAME,
                              TestData.ADDRESS,
                              order_page.select_metro_station_1, TestData.PHONE, TestData.DATE,
                              order_page.select_time_1, order_page.select_scooter_color_1,
                              TestData.COMMENT)

        with allure.step("Verify order success message"):
            assert "Заказ оформлен" in driver.page_source

    @allure.title("Make order two")
    @allure.severity(allure.severity_level.NORMAL)
    def test_make_order_two(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.BASE_URL)

        perform_order_process(order_page, order_page.click_order_button_down, TestData.NAME_1, TestData.LAST_NAME_1,
                              TestData.ADDRESS_1,
                              order_page.select_metro_station_2, TestData.PHONE_1, TestData.DATE_1,
                              order_page.select_time_2, order_page.select_scooter_color_2,
                              TestData.COMMENT_1)

        with allure.step("Verify order success message"):
            assert "Заказ оформлен" in driver.page_source

    @allure.title("Click logo redirect to dzen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_logo_redirect_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.BASE_URL)

        with allure.step("Click Yandex logo"):
            order_page.click_yandex_button()

        # Добавим ожидание перенаправления
        allure.attach(driver.current_url, name="Current URL")
        assert "https://dzen.ru/" in driver.current_url

    @allure.title("Click logo redirect to samokat")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_logo_redirect_to_samokat(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_URL)

        with allure.step("Click Samokat logo"):
            order_page.click_samocat_button()

        # Уберем лишний символ "="
        allure.attach(driver.current_url, name="Current URL")
        assert TestData.BASE_URL == driver.current_url
