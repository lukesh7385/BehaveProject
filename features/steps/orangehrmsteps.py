from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('Launch chrome browser')
def LaunchBrowser(context):
    serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
    context.driver = webdriver.Chrome(service=serv_obj)


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
