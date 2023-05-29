import random
from Pages.base_page import BasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randrange
from selenium.webdriver.common.by import By

class LocatorsRegistration:
    FIRST_NAME_IN=(By.XPATH,'//input[@id="UserFirstName"]')
    SURNAME_IN=(By.XPATH,'//input[@id="UserLastName"]')
    EMAIL_IN=(By.XPATH,'//input[@id="UserEmail"]')
    PASSWORD_IN=(By.XPATH,'//input[@id="UserPasswd"]')
    STATUTE_CHECK=(By.XPATH,'//*[@id="UserRegisterForm"]/div[2]/div[7]/span/a')
    ALL_CHECKBOXES=(By.XPATH,'//div[@class="form-inner form-inner-wider form-inner-left"]/div/span[@class="transform-checkbox-wrapper transform-wrapper" or class="transform-checkbox-wrapper transform-wrapper"]')
    CREATE_ACCOUNT=(By.XPATH,'//input[@class="btn-block btn btn-primary btn-lg"]')
    DROPDAYCLASS=(By.XPATH,'//ul[@class="transform-select-list transform-search-box-true open"]/li')
    DROPMONTHCLASS=(By.XPATH,'//ul[@class="transform-select-list transform-search-box-true open"]/li')
    DROPYEARCLASS=(By.XPATH,'//ul[@class="transform-select-list transform-search-box-true open"]/li')
    ALLDROP=(By.XPATH,'//div[@class="transform-select transform-input form-control"]/a[@class="transform-open"]')
    TELEPHONE=(By.ID,"UserPhone")
    INFOTWOCHECBOX=(By.XPATH,'//*[@id="UserRegisterForm"]/div[2]/div[13]/div')

class RegistrationPage(BasePage):
    def _verify_page(self):
        """Autoweryfikacja str glownej"""
        pass

    def generator_telephonnumber(self):

        i = 0
        while i < 9:
            if i == 0:
                num1 = random.randrange(1, 10)
                telnumber = str(num1)
                i = i + 1
            else:
                num2 = random.randrange(0, 10)
                telnumber = telnumber + str(num2)
                i = i + 1
        return str(telnumber)


    def complete_form(self,name,surname,email,password):
        self.driver.find_element(*LocatorsRegistration.FIRST_NAME_IN).send_keys(name)
        self.driver.find_element(*LocatorsRegistration.SURNAME_IN).send_keys(surname)
        self.driver.find_element(*LocatorsRegistration.EMAIL_IN).send_keys(email)
        self.driver.find_element(*LocatorsRegistration.PASSWORD_IN).send_keys(password)
        number=self.generator_telephonnumber()
        self.driver.find_element(*LocatorsRegistration.TELEPHONE).send_keys(number)

    def click_dayofbirthday(self,d):

        w=self.driver.find_elements(*LocatorsRegistration.ALLDROP)
        w[2].click()
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(d)
        sleep(2)
        classday=self.driver.find_elements(*LocatorsRegistration.DROPDAYCLASS)
        k=0
        for i in classday:
            if k==d:
                i.click()
                break
            k=k+1
        sleep(3)

    def click_monthofbirthday(self,d):

        w=self.driver.find_elements(*LocatorsRegistration.ALLDROP)
        w[1].click()
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(d)

        classmonth=self.driver.find_elements(*LocatorsRegistration.DROPMONTHCLASS)
        k=0
        for i in classmonth:
            if k==d:
                #print(i.text)
                i.click()
                break
            k=k+1
    def click_yearofbirthday(self,d):
        w=self.driver.find_elements(*LocatorsRegistration.ALLDROP)
        w[0].click()

        action=ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(d)
        sleep(2)
        classyear=self.driver.find_elements(*LocatorsRegistration.DROPYEARCLASS)
        k=1944
        for i in classyear:
            if k==d:
                i.click()
                break
            k=k+1

    def find_all_checboxes(self):
        self.checboxes = self.driver.find_elements(*LocatorsRegistration.ALL_CHECKBOXES)

        return self.checboxes

    def click_checkbox(self,number):
        self.checboxes=self.find_all_checboxes()
        self.checboxes[number].click()

    def clean_all_checkboxes(self):
        self.checboxes=self.find_all_checboxes()
        for checkbox in self.checboxes:
            if checkbox.is_selected():
                checkbox.click()
    def click_buttom(self,selector):
        self.driver.find_element(*selector).click()

    def take_message(self,selector):
        w=self.driver.find_element(*selector).text
        return w

