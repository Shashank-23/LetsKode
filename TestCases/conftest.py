import pytest
from selenium import webdriver

@pytest.fixture()
def initialize():
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome("C:\\Users\\e01710\\PycharmProjects\\Flipkart\\Resources\\chromedriver.exe")
    driver.get(baseURL)
    print("Running tests on chrome")
    driver.implicitly_wait(10)

