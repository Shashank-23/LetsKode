import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


# @pytest.mark.usefixtures("initialize")
class testLogin(framework_Utility,unittest.TestCase):

    def test_login(self,initialize):
        f = framework_Utility(self.driver)
        f.clickElement("link_text","Login")