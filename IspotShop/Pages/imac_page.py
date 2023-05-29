from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LocatorsiMacPage:
        WRITENIMAC=(By.XPATH,'/html/body/div[5]/div/div/section/div/div[1]/h1')
        ALLPRODUCTS=(By.XPATH,'//ul[@class="categories-boxes"]/li')

class ImacPage(BasePage):


    def getproducts(self):
        w=self.driver.find_elements(*LocatorsiMacPage.ALLPRODUCTS)
        return w




