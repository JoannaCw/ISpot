from Tests.base_test import BaseTest
from Data.valid_data import Validdata
from Pages.products_page import ProductsPage
from Pages.products_page import LocatorsProducts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page.click_cookies()
        self.home_page.search_product(Validdata.product)
        self.product_page=ProductsPage(self.driver)

    def test_add_to_schoppingcard(self):
        wait=WebDriverWait(self.driver,5)
        self.product_page.click_button(LocatorsProducts.ADD_CARD)
        wait.until((EC.element_to_be_clickable(LocatorsProducts.BUTTON_NEXT)))
        self.product_page.click_button(LocatorsProducts.BUTTON_NEXT)
        wait.until(EC.presence_of_element_located(LocatorsProducts.TEXT_AFTER_ADD))
        w=self.product_page.get_text(LocatorsProducts.TEXT_AFTER_ADD)
        self.assertEquals("Produkt dodano do koszyka",w,"Komunikat o dodaniu prdduktu nie pojawil sie")

    def test_correct_product(self):
        text=self.product_page.get_text(LocatorsProducts.TEXTSEARCHPPRODUCT)
        product_correct=Validdata.product
        self.assertEquals(product_correct,text,"Niepoprawne wyszukanie")
    def test_correct_price(self):
        price_correct=Validdata.price
        price=self.product_page.get_price_product(LocatorsProducts.PRICE_PRODUCT)
        print(price)
        self.assertEquals(price_correct,price,"cena na stronie nie jest poprawna")

