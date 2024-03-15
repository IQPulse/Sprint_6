# Sprint_6
Финальный проект 6 спринт

# Автоматизированные тесты для сайта по заказу самокатов

Этот проект содержит автоматизированные тесты для веб-приложения по заказу самокатов. Тесты написаны с использованием Python, Selenium WebDriver и фреймворка Pytest.

## Инструкции по запуску

1. Убедитесь, что у вас установлен Python и Mozilla Firefox.

2. Для запуска всех тестов выполните команду:

    ```
    pytest -v
    ```

3. Для запуска отдельных тестов выполните соответствующую команду:

    ```
    pytest -v tests/test_main_page.py::TestMainPageQuestions
    pytest -v tests/test_order_page.py::TestOrderPage::test_make_order_one
    pytest -v tests/test_order_page.py::TestOrderPage::test_make_order_two
    pytest -v tests/test_order_page.py::TestOrderPage::test_click_logo_redirect_to_dzen
    pytest -v tests/test_order_page.py::TestOrderPage::test_click_logo_redirect_to_samokat
    ```

4. Для получения отчета Allure выполните следующие команды:

    ```
    pytest --alluredir=allure_results
    allure serve allure_results
    ```

## Содержание проекта

- `locators/`: Папка с файлами, содержащими локаторы элементов на веб-страницах.
- `pages/`: Папка с файлами, содержащими классы страниц и их методы.
- `tests/`: Папка с файлами, содержащими тесты.
- `conftest.py`: Файл с фикстурами и общими настройками для тестов.
- `helpers.py`: Файл с вспомогательными функциями для тестов.
- `data.py`: Файл с тестовыми данными.
