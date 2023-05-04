from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class WebElement:

    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.driver.find_element(By.CSS_SELECTOR, self.locator).click()

    def find_element(self):
        self.driver.find_element(By.CSS_SELECTOR, self.locator).click()

    def exist_icon(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True
