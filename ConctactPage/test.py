import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from contact_page import ContactPage

@pytest.fixture
def driver():
    options = Options()
    # Эти три флага нужны для работы Chrome в CI (в контейнере без дисплея)
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
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

