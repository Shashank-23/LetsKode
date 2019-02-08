import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def launchBrowser():
    baseURL = "https://letskodeit.teachable.com/"
    browserName = "chrome"

    if browserName is "chrome":
        print("Running tests on Google Chrome")
        driver = webdriver.Chrome("C:\\Users\\e01710\\PycharmProjects\\LetsKode\\Resources\\chromedriver.exe")
    elif browserName is "firefox":
        print("Running tests on Mozilla Firefox")
        driver = webdriver.Firefox("C:\\Users\\e01710\\PycharmProjects\\LetsKode\\Resources\\geckodriver.exe")
    else:
        print("Browser Not Specified")
        exit(0)

    driver.get(baseURL)

    yield driver
    driver.quit()

