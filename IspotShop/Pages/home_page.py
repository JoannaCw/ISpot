from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Pages.imac_page import ImacPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocatorsHome:
    LOGIN_LINK=(By.XPATH,'//div/a[@href="/logowanie"]')
    SHOPPING_CART=(By.XPATH,'//div[@class="header-nav-item"]/a[@href="/koszyk"]')
    SEARCH_INPUT=(By.XPATH,'//input[@id="ProductQ2"]')
    WATCH_CART=(By.XPATH,"//a[@href='/apple-watch']")
    COOKIES=(By.XPATH,"//a[@href='/users/accept_cookies']")
    SMALLMENU=(By.XPATH,"//div[@class='navbar']/a")
    MAINMENU=(By.XPATH,'//ul[@id="MainNav"]/li[@class="with-images" or @class=""]')
    MACMENU=(By.XPATH,"//a[@title='Mac']")
    MACPRODUCTS=(By.XPATH,'//div[@data-id="2"]/div[@class="sub-categories"]')
    MACPRODUCT=(By.XPATH,'//a[@href="/mac"]')
    MY_ACCOUNT=(By.XPATH,'//a[@href="/edycja-konta" and @title="Na skróty"]')
    MACPRODUCT2=(By.XPATH,'//div[@class ="sub-cat open"]/div')



class HomePage(BasePage):
    def _verify_page(self):
        """Autoweryfikacja str glownej"""
        pass

    def click_cookies(self):
        self.driver.find_element(*LocatorsHome.COOKIES).click()

    def click_login(self):
        self.driver.find_element(*LocatorsHome.LOGIN_LINK).click()
        return LoginPage(self.driver)

    def itemssmallmenu(self):
        w=self.driver.find_elements(*LocatorsHome.SMALLMENU)
        return w

    def click_shoppingcard(self):
        self.driver.find_element(*LocatorsHome.SHOPPING_CART).click()


    def writing_search(self,word):
        self.driver.find_element(*LocatorsHome.SEARCH_INPUT).send_keys(word, Keys.RETURN)
        return ProductsPage(self.driver)

    def itemsmainmenu(self):
        w=self.driver.find_elements(*LocatorsHome.MAINMENU)
        return w

    def movetoMAC(self):
        action=ActionChains(self.driver)
        w=self.driver.find_element(*LocatorsHome.MACMENU)
        action.move_to_element(w)
        action.perform()
        products=self.driver.find_elements(*LocatorsHome.MACPRODUCT2)
        return products


    def clickProductMac(self):
        self.movetoMAC()
        wait=WebDriverWait(self.driver,6)
        kop=wait.until(EC.element_to_be_clickable(self.driver.find_element(*LocatorsHome.MACPRODUCT))).click()
        return ImacPage(self.driver)

    def click_buttom(self,selector):
        self.driver.find_element(*selector).click()
    def search_product(self,Data):
        self.writing_search(Data)

