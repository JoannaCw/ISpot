from Pages.base_page import BasePage
from Pages.shoppingcart_page import ShoppingPage
from selenium.webdriver.common.by import By

class LocatorsProducts:
    WRITTINGPRODUCTS=(By.XPATH,"/html/body/div[5]/div/div/section/div/div[1]/h1")
    TEXTSEARCHPPRODUCT=(By.XPATH,'// div[@class ="product-header page-header"]')
    search_product=(By.XPATH,'//div[@class="product-header page-header"]')
    PRICE_PRODUCT=(By.XPATH,'//span[@class="price new-price"]')
    ADD_CARD=(By.XPATH,'//div[@class="hidden-xs"]/div[@class="product-actions button-hold"]')
    POP_UP_FRAME=(By.XPATH,'//div[@class="service-insurance-modal modal-wide modal fade in"]/div[@class="modal-dialog"]')
    CLOSE_POPUP=(By.XPATH,'//div[@id="ServiceInsurance0"]/div[@class="modal-dialog"]/div[@class="modal-content"]/div[@class="modal-header"]/button[@class="close"]')
    SCHOPPINGCARD=(By.XPATH,'/html/body/div[3]/header/div[2]/div/div[4]/ul/li[3]/div[1]/a')
    BUTTON_NEXT=(By.XPATH,'//button[@class="btn-next btn btn-primary btn-lg"]')
    TEXT_AFTER_ADD=(By.XPATH,'//div[@class="modal-header"]/h2')

class ProductsPage(BasePage):

    def click_button(self,selector):
         self.driver.find_element(*selector).click()
    def get_price_product(self,selector):
        price=self.driver.find_element(*selector).get_attribute("data-price")
        return price
    def get_text(self, selector):
        w=self.driver.find_element(*selector).text
        return w
    def go_to_shoppingcard(self):
        self.driver.find_element(LocatorsProducts.SCHOPPINGCARD).click()
        return ShoppingPage(self.driver)
