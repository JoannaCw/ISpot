from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.home_page import LocatorsHome
from Pages.login_page import LocatorsLogin
from Data.valid_data import Validdata
from Data.invalid_data import Invaliddata
from time import sleep

class LoginTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page.click_cookies()
        self.driver.find_element(*LocatorsHome.LOGIN_LINK).click()
        self.login_page=LoginPage(self.driver)
        self.driver.switch_to.frame(self.login_page.wait_for_element(LocatorsLogin.POP_UP_FRAME, 20))
        self.login_page.wait_for_element(LocatorsLogin.SEND_LETTER_POP_UP, 20)
        self.login_page.custom_find_element(LocatorsLogin.CLOSE_BTN).click()
        self.driver.switch_to.default_content()


    def test_Register_click(self):
        self.login_page.buttom_click(LocatorsLogin.REGISTER_BUTTON)
        el=self.login_page.get_message(LocatorsLogin.WRITTING_REGISTRATION)
        self.assertEqual("Rejestracja",el)

    def test_correctlogin(self):
        self.login_page.enter_email(Validdata.email)
        self.login_page.enter_password(Validdata.password)
        self.login_page.log_in_click()
        w=self.login_page.find_my_account().text
        self.assertEqual("Twoje konto",w,"Próba logowania nie powiodła się")

    def test_enter_inncorrect_email(self):
        self.login_page.enter_email(Invaliddata.email)
        self.login_page.enter_password(Validdata.password)
        self.login_page.log_in_click()
        k=self.login_page.get_message(LocatorsLogin.WRONG_EMAILPASS_MESSAGE)
        self.assertEqual("Niepoprawna nazwa użytkownika lub hasło!\n×",k,"Proba zalogowania z niepoprawym email nie powiodła się")


    def test_enter_inncorrect_password(self):
        self.login_page.enter_email(Validdata.email)
        self.login_page.enter_password(Invaliddata.password)
        self.login_page.log_in_click()
        k = self.login_page.get_message(LocatorsLogin.WRONG_EMAILPASS_MESSAGE)
        self.assertEqual("Niepoprawna nazwa użytkownika lub hasło!\n×",k,"Proba zalogowania z niepoprawym email nie powiodła się")

    def test_login_inncorrect_date(self):
        self.login_page.enter_email(Invaliddata.email)
        self.login_page.enter_password(Invaliddata.password)
        self.login_page.log_in_click()
        k = self.login_page.get_message(LocatorsLogin.WRONG_EMAILPASS_MESSAGE)
        self.assertEqual("Niepoprawna nazwa użytkownika lub hasło!\n×",k,"Proba zalogowania z niepoprawym email nie powiodła się")

    def test_passwordreminder(self):
        self.login_page.click_buttom(LocatorsLogin.REMINDER_PASSWORD)
        self.login_page.enteremail_reminder(Validdata.email)
        self.login_page.click_buttom(LocatorsLogin.REMINDER_PASSWORD_LAST_BUTTON)
        sleep(2)
        w=self.login_page.get_message(LocatorsLogin.MESSAGE_2)
        self.assertEqual("Jeżeli użytkownik o podanym adresie e-mail istnieje w naszej bazie danych to została na niego wysłana wiadomość z instrukacjami jak uzyskać nowe hasło.\n×",w)
















