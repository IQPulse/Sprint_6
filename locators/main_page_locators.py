from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOCATOR = (By.XPATH, '//div[@id="accordion__heading-{}"]') # вопрос
    ANSWER_LOCATOR = (By.CSS_SELECTOR, 'div[id="accordion__panel-{}"] p') # ответ
    MAIN_PAGE_TEXT = (By.XPATH, "//div[@class='Home_Header__iJKdX']") # текст ответа
    MAIN_PAGE_COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']") # кнопка "да все привыкли"
    BUTTON_ORDER_DOWN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")  # кнопка Заказать нижняя