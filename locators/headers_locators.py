from selenium.webdriver.common.by import By

class HeadersLocators:

    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']") # логотип Yandex
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']") # логотип Самокат
    BUTTON_ORDER_UP = (By.XPATH, "//button[@class='Button_Button__ra12g']") # кнопка Заказать верх