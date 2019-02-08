import pytest
import unittest
from POM.loginPage import loginPage

class testLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, launchBrowser):
        driver = launchBrowser
        self.loginPageObj = loginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.loginPageObj.enterEmail("test@email.com")
        self.loginPageObj.enterPassword("abcabc")
        self.loginPageObj.clickBtnLogin()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.loginPageObj.clickLinkLogin()
        self.loginPageObj.enterEmail("test@email.com")
        self.loginPageObj.enterPassword("invalidPass")
        self.loginPageObj.clickBtnLogin()


