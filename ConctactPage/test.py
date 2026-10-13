import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from contact_page import ContactPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_submit(driver):
    page = ContactPage(driver).open_page()

    page.fill_form(
        name="Иван Иванов",
        email="ivan@example.com",
        subject="Запрос консультации",
        message="Здравствуйте! Хочу получить консультацию по вашему продукту.",
    ).submit()

    assert page.is_success_visible(), "Сообщение об успехе не появилось"
    assert "Спасибо" in page.get_success_text()

def test_submit_with_empty_name(driver):
    page = ContactPage(driver).open_page()

    page.fill_form(
        name="",
        email="ivan@example.com",
        subject="Запрос консультации",
        message="Здравствуйте! Хочу получить консультацию.",
    ).submit()

    assert "Имя обязательно" in page.get_name_error()
    assert not page.is_success_visible(), "Форма не должна отправляться"

