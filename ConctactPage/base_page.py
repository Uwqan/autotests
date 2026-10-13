from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = "http://127.0.0.1:5000"
    DEFAULT_TIMEOUT = 3

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, path=""):
        self.driver.get(self.BASE_URL + path)
        return self

    def wait_visible(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def type(self, by, value, text):
        element = self.wait_visible(by, value)
        element.clear()
        element.send_keys(text)
        return self

    def click(self, by, value):
        element = self.wait_visible(by, value)
        element.click()
        return self

    def get_text(self, by, value):
        return self.wait_visible(by, value).text

    def is_visible(self, by, value, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except Exception:
            return False

    def current_url(self):
        return self.driver.current_url