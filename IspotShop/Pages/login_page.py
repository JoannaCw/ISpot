from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LocatorsLogin:
    WRITING_LOGIN=(By.XPATH,"/html/body/div[5]/div/div/section/div/div[1]/h1")
    REGISTER_BUTTON=(By.XPATH, '//a[@href="/rejestracja"]')
    WRITTING_REGISTRATION=(By.XPATH,'//div[@class="page-header"]/h1')
    EMAIL_INPUT=(By.XPATH,"//div[@class='form-inner']/div[@class='form-row']/input[@id='UserEmail']")
    PASSWORD_INPUT=(By.XPATH,"//input[@id='UserPassword']")
    LOG_IN_BUTTON=(By.XPATH,"//*[@id='UserLoginForm']/div[2]/div[5]/input")
    MY_ACCOUNT=(By.XPATH,'//div[@class="user-status-info header-nav-item"]/a[@href="/edycja-konta"]')
    CLOSE_NEWS=(By.XPATH,"//*[@id='edrone-onsite-popup-content']/div/div/div[2]")
    MESSAGE_1=(By.XPATH,'/html/body/div[5]/div/div/section/div[1]/span[1]')
    REMINDER_PASSWORD=(By.XPATH,'//a[@title="Przypomnij hasło"]')
    FORM=(By.ID,'UserPasswordRemindForm')
    EMAIL_INPUTREMINDER=(By.XPATH,"//form[@id='UserPasswordRemindForm']/div[2]/div/input[@id='UserEmail']")
    REMINDER_PASSWORD_LAST_BUTTON=(By.XPATH,'//*[@id="UserPasswordRemindForm"]/div[2]/div[3]/input')
    MESSAGE_2=(By.XPATH,'//div[@class="message info"]')
    MY_DATA=(By.XPATH,'//div[@class="page-content page-sidebar-true"]/div[@class="page-header"]')
    POP_UP_FRAME=(By.XPATH, "//iframe[@id='edrone-onsite-popup-iframe']")
    SEND_LETTER_POP_UP = (By.XPATH, "//*[contains(text(), 'Zapisz się do newslettera iSpot')]/ancestor::div[@class='mobile-below']")
    CLOSE_BTN = (By.CSS_SELECTOR, "div > svg[fill='none']")
    REGGISTRARION=(By.XPATH,'// a[ @ title = "Zarejestruj się"]')
    WRONG_EMAILPASS_MESSAGE=(By.XPATH,'// div[@class ="auth-error message info"]')

class LoginPage(BasePage):
    def _verify_page(self):
        pass

    def buttom_click(self,selector):
        self.driver.find_element(*selector).click()
    def enter_email(self,email):
        el=self.driver.find_element(*LocatorsLogin.EMAIL_INPUT)
        el.send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*LocatorsLogin.PASSWORD_INPUT).send_keys(password)

    def log_in_click(self):
        self.driver.find_element(*LocatorsLogin.LOG_IN_BUTTON).click()

    def find_my_account(self):
        return self.driver.find_element(*LocatorsLogin.MY_ACCOUNT)

    def get_message(self,selector):
        w=self.driver.find_element(*selector)
        return w.text

    def click_buttom(self,selector):
        self.driver.find_element(*selector).click()

    def enteremail_reminder(self,email):
        self.driver.find_element(*LocatorsLogin.EMAIL_INPUTREMINDER).send_keys(email)

    def custom_find_element(self, selector):
        return self.driver.find_element(selector[0],selector[1])

    def wait_for_element(self, selector, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(selector))
            return self.driver.find_element(selector[0], selector[1])
        except TimeoutException:
            raise TimeoutException('Web Element with {} locator hasn\'t been found for the provided timeout {}'.
                                   format(selector, timeout))








