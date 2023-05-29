from Tests.base_test import BaseTest
from time import sleep

class IMacTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page.click_cookies()
        self.imac_page=self.home_page.clickProductMac()
        sleep(3)

    def test_itemsproducts(self):
        items=self.imac_page.getproducts()
        self.assertEqual(12,len(items),"Liczba produktów na stronie iMac nie zgadza się")
