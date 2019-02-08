from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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

    def waitforXseconds(self,seconds):
        self.driver.implicitly_wait(seconds)

    # def waitForElementVisibility(self,locatorName, locatorValue):
    #     wait = WebDriverWait(self.driver, 10, poll_frequency=0.5)
    #     wait.until(EC.)

    def getElement(self,locatorName, locatorValue):
         # print(self.getByType(locatorName))
         # print(locatorValue)
         byType = self.getByType(locatorName)
         element = self.driver.find_element(byType,locatorValue)
         return element


    def getElements(self, locatorName, locatorValue):
        byType = self.getByType(locatorName)
        element = self.driver.find_elements(byType, locatorValue)
        return element

    def clickElement(self, locatorName, locatorValue):
        # print("Running clickElement")
        element = self.getElement(locatorName, locatorValue)
        element.click()

    def enterValue(self, locatorName, locatorValue, data):
        element = self.getElement(locatorName, locatorValue)
        element.clear()
        element.send_keys(data)
