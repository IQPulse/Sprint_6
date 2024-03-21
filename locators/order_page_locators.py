from selenium.webdriver.common.by import By

class OrderPageLocators:

    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']") # поле Имя
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле Фамилия
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поле Адрес: куда привезти заказ
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле Телефон: на него позвонит курьер
    SELECT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']") # выпадающий список Станция метро
    SELECT_METRO_STATION_1 = (By.CSS_SELECTOR, "li.select-search__row:nth-child(1)") # 1-я станция метро из выпадающего списка
    SELECT_METRO_STATION_2 = (By.CSS_SELECTOR, "li.select-search__row:nth-child(2)") # 2-я станция метро из выпадающего списка
    BUTTON_NEXT = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") # кнопка Далее
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле Когда привезти самокат
    SELECT_TIME = (By.XPATH, "//div[@class='Dropdown-placeholder']") # поле Срока аренды
    SELECT_TIME_DAY_1 = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(1)") # сутки из выпадающего списка
    SELECT_TIME_DAY_2 = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(2)") # двое суток
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # поле Комментарий для курьера
    BUTTON_COLOR_1 = (By.XPATH, "//input[@id='black']") # в поле Цвет самоката: чёрный жемчуг
    BUTTON_COLOR_2 = (By.XPATH, "//input[@id='grey']") # в поле Цвет самоката: серая безысходность
    BUTTON_SUBMIT = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") # Кнопка Заказать после заполнения формы
    BUTTON_YES = (By.XPATH, "//button[contains(text(),'Да')]") # кнопка Заказать
    TEXT_ORDER_CONFIRMED = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]") # в модальном окне "Хотите оформить заказ?" кнопка Да
