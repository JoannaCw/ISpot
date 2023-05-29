from Tests.base_test import BaseTest
from Pages.home_page import LocatorsHome
from Pages.login_page import LocatorsLogin
from Pages.login_page import LoginPage
from Pages.registration_page import RegistrationPage
from Pages.registration_page import LocatorsRegistration
from Data.invalid_data import Invaliddata
from Data.valid_data import Validdata

class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page.click_cookies()
        self.driver.find_element(*LocatorsHome.LOGIN_LINK).click()
        self.login_page = LoginPage(self.driver)
        self.driver.switch_to.frame(self.login_page.wait_for_element(LocatorsLogin.POP_UP_FRAME, 20))
        self.login_page.wait_for_element(LocatorsLogin.SEND_LETTER_POP_UP, 20)
        self.login_page.custom_find_element(LocatorsLogin.CLOSE_BTN).click()
        self.driver.switch_to.default_content()
        self.driver.find_element(*LocatorsLogin.REGISTER_BUTTON).click()
        self.registration_page=RegistrationPage(self.driver)

    def test_correctcompleteform(self):
        self.registration_page.complete_form(Invaliddata.name,Invaliddata.last_name,Invaliddata.email,Invaliddata.password)
        self.registration_page.click_yearofbirthday(Validdata.year)
        self.registration_page.click_monthofbirthday(Validdata.month)
        self.registration_page.click_dayofbirthday(Validdata.day)
        self.registration_page.click_checkbox(0)
        self.registration_page.click_checkbox(1)
       #self.registration_page.click_buttom(LocatorsRegistration.CREATE_ACCOUNT) """celowo kod jest w komentarzu aby nie założyć konta, nie daje również celowo asercjii."""

    def test_onlyonechecbox(self):
        self.registration_page.complete_form(Invaliddata.name,Invaliddata.last_name,Invaliddata.email,Invaliddata.password)
        self.registration_page.click_yearofbirthday(Validdata.year)
        self.registration_page.click_monthofbirthday(Validdata.month)
        self.registration_page.click_dayofbirthday(Validdata.day)
        self.registration_page.click_checkbox(0)
        self.registration_page.click_buttom(LocatorsRegistration.CREATE_ACCOUNT)
        w=self.registration_page.take_message(LocatorsRegistration.INFOTWOCHECBOX)
        self.assertEqual("Proszę uzupełnić to pole.",w)







