import allure
from pages.order_page import OrderPage
from data import TestData

class TestOrderPage:
    @allure.feature("Order Page")
    @allure.story("Order Process")
    @allure.title("Make order one")
    @allure.severity(allure.severity_level.NORMAL)
    def test_make_order_one(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(TestData.BASE_URL)

        with allure.step("Click order button"):
            order_page.click_order_button_up()
        with allure.step("Enter name"):
            order_page.input_name(TestData.NAME)
        with allure.step("Enter last name"):
            order_page.input_last_name(TestData.LAST_NAME)
        with allure.step("Enter address"):
            order_page.input_address(TestData.ADDRESS)
        with allure.step("Select metro station"):
            order_page.select_metro_station_1()
        with allure.step("Enter phone number"):
            order_page.input_phone(TestData.PHONE)
        with allure.step("Click next button"):
            order_page.click_next_button()
        with allure.step("When to bring the scooter"):
            order_page.input_date(TestData.DATE)
        with allure.step("The rental period"):
            order_page.select_time_1()
        with allure.step("Select scooter color"):
            order_page.select_scooter_color_1()
        with allure.step("Enter comment"):
            order_page.input_comment(TestData.COMMENT)
        with allure.step("Click submit button"):
            order_page.click_submit_button()
        with allure.step("Click yes button"):
            order_page.click_yes_button()

        with allure.step("Verify order success message"):
            assert "Заказ оформлен" in driver.page_source

    @allure.feature("Order Page")
    @allure.story("Order Process")
    @allure.title("Make order two")
    @allure.severity(allure.severity_level.NORMAL)
    def test_make_order_two(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(TestData.BASE_URL)

        with allure.step("Click order button"):
            order_page.click_order_button_down()
        with allure.step("Enter name"):
            order_page.input_name(TestData.NAME_1)
        with allure.step("Enter last name"):
            order_page.input_last_name(TestData.LAST_NAME_1)
        with allure.step("Enter address"):
            order_page.input_address(TestData.ADDRESS_1)
        with allure.step("Select metro station"):
            order_page.select_metro_station_2()
        with allure.step("Enter phone number"):
            order_page.input_phone(TestData.PHONE_1)
        with allure.step("Click next button"):
            order_page.click_next_button()
        with allure.step("When to bring the scooter"):
            order_page.input_date(TestData.DATE_1)
        with allure.step("The rental period"):
            order_page.select_time_2()
        with allure.step("Select scooter color"):
            order_page.select_scooter_color_2()
        with allure.step("Enter comment"):
            order_page.input_comment(TestData.COMMENT_1)
        with allure.step("Click submit button"):
            order_page.click_submit_button()
        with allure.step("Click yes button"):
            order_page.click_yes_button()

        with allure.step("Verify order success message"):
            assert "Заказ оформлен" in driver.page_source

    @allure.feature("Order Page")
    @allure.story("Navigation")
    @allure.title("Click logo redirect to dzen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_logo_redirect_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(TestData.BASE_URL)

        with allure.step("Click Yandex logo"):
            order_page.click_yandex_button()

        with allure.step("Verify redirection to Dzen"):
            assert driver.title == TestData.DZEN_LOGO and driver.current_url == TestData.DZEN_URL_REDIRECT

    @allure.feature("Order Page")
    @allure.story("Navigation")
    @allure.title("Click logo redirect to samokat")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_logo_redirect_to_samokat(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(TestData.ORDER_URL)

        with allure.step("Click Samokat logo"):
            order_page.click_samocat_button()

        with allure.step("Verify redirection to Samokat"):
            assert TestData.BASE_URL == driver.current_url
