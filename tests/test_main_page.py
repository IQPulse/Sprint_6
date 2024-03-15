import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import MainPageAnswers

class TestMainPageQuestions:
    @allure.feature("Main Page")
    @allure.story("Questions")
    @allure.title("Test question {q_num}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "q_num, expected_result",
        [
            (0, MainPageAnswers.main_page_answer_0),
            (1, MainPageAnswers.main_page_answer_1),
            (2, MainPageAnswers.main_page_answer_2),
            (3, MainPageAnswers.main_page_answer_3),
            (4, MainPageAnswers.main_page_answer_4),
            (5, MainPageAnswers.main_page_answer_5),
            (6, MainPageAnswers.main_page_answer_6),
            (7, MainPageAnswers.main_page_answer_7),
        ]
    )
    def test_questions(self, driver, q_num, expected_result):
        main_page = MainPage(driver)
        with allure.step(f"Clicking on question {q_num}"):
            result = main_page.click_to_question_and_get_answer_text(MainPageLocators.QUESTION_LOCATOR, q_num)
        with allure.step(f"Verifying answer for question {q_num}"):
            assert result == expected_result
