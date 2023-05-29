from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
class LocatorsShoppingcart:

    WRITING_CART=(By.XPATH, "/html/body/div[4]/div/div/section/div/div[1]/h1")

class ShoppingPage(BasePage):
    def _verify_page(self):
        self.wait=WebDriverWait(self.driver,6)