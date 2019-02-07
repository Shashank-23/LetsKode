import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class framework_Utility():

    def __init__(self,driver):
        self.driver = driver

    def getByType(self, locatorName):
         locatorName.lower()
         switcher = {
             "id" : By.ID,
             "name" : By.NAME,
             "link_text" : By.LINK_TEXT
         }
         return switcher.get(locatorName)

    def getElement(self,locatorName, locatorValue):
         print(self.getByType(locatorName))
         print(locatorValue)
         byType = self.getByType(locatorName)
         element = self.driver.find_element(byType,locatorValue)
         return element


    def getElements(self, locatorName, locatorValue):
         return self.driver.find_elements(self.getByType(locatorName),locatorValue)

    def clickElement(self, locatorName, locatorValue):
        print("Running clickElemet")
        self.getElement(locatorName, locatorValue).click()

