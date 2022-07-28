from tabnanny import check
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.config import default_wait_timeout


class TrianglePage:
    page_url = 'https://playground.learnqa.ru/puzzle/triangle'

    side_a_selector = (By.CSS_SELECTOR, '.js_a')
    side_b_selector = (By.CSS_SELECTOR, '.js_b')
    side_c_selector = (By.CSS_SELECTOR, '.js_c')
    check_button_selector = (By.CSS_SELECTOR, '.btn.btn-submit')
    text_field_selector = (By.CSS_SELECTOR, '.info.logg')

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.page_url)

    def fill_side(self, locator, text_to_write):
        element = WebDriverWait(self.driver, default_wait_timeout).until(EC.presence_of_element_located(locator))
        element.send_keys(text_to_write)

    def click_check_button(self):
        element = WebDriverWait(self.driver, default_wait_timeout).until(EC.presence_of_element_located(self.check_button_selector))
        ActionChains(self.driver).click(element).perform()

    def get_text_field_value(self):
        element = WebDriverWait(self.driver, default_wait_timeout).until(EC.presence_of_element_located(self.text_field_selector))
        return element.text

    def clear_fields(self):
        WebDriverWait(self.driver, default_wait_timeout).until(EC.presence_of_element_located(self.side_a_selector)).clear()
        WebDriverWait(self.driver, default_wait_timeout).until(EC.presence_of_element_located(self.side_b_selector)).clear()
        WebDriverWait(self.driver, default_wait_timeout).until(EC.presence_of_element_located(self.side_c_selector)).clear()
