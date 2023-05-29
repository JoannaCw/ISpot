from Tests.base_test import BaseTest
from Pages.products_page import LocatorsProducts
from Pages.login_page import LocatorsLogin
from Pages.shoppingcart_page import LocatorsShoppingcart
from time import sleep

class HomeTest(BaseTest):

     def setUp(self):
         super().setUp()
         self.home_page.click_cookies()

     def test_login_click(self):
        self.home_page.click_login()
        el=self.driver.find_element(*LocatorsLogin.WRITING_LOGIN).text
        self.assertEqual("Logowanie",el)

     def test_shoppingcard(self):
        self.home_page.click_shoppingcard()
        sleep(2)
        el=self.driver.find_element(*LocatorsShoppingcart.WRITING_CART).text
        self.assertEqual("Koszyk", el)

     def test_titlewindow(self):
        el=self.driver.title
        self.assertEqual("iSpot Apple Sklep internetowy - Apple Premium Reseller Polska",el)

     def test_search_input(self):
        self.home_page.writing_search("ipad")
        sleep(2)
        el=self.driver.find_element(*LocatorsProducts.WRITTINGPRODUCTS).text
        sleep(2)
        self.assertEqual("Produkty", el)

     def test_smallmenu(self):
         el=self.home_page.itemssmallmenu()
         size=len(el)
         self.assertTrue(size==5,"małe menu nie jest widoczne")

     def test_mainmenu(self):
          el=self.home_page.itemsmainmenu()
          size=len(el)
          self.assertTrue(size==9,"główne menu nie jest widoczne")

     def test_movetomac(self):
        items=self.home_page.movetoMAC()
        self.assertTrue(len(items)==12,"Nie widać wszystkich produktów w MACMenu")

     def test_clickmac(self):
        self.home_page.clickProductMac()
        w=self.driver.current_url
        self.assertEqual("https://ispot.pl/mac",w, "Nie przeszlo do zakładki imac")

