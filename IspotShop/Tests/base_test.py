import unittest
from selenium import webdriver
from Pages.home_page import HomePage

class BaseTest(unittest.TestCase):

    def setUp(self):
        """warunki wstepne kazdego testu"""
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://ispot.pl/")
        self.home_page=HomePage(self.driver)

    def tearDown(self):
        """zamknięcie przeglądarki"""
        self.driver.quit()