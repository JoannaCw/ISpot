from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self._verify_page()

    def _verify_page(self):
        self.wait=WebDriverWait(self.driver,6)