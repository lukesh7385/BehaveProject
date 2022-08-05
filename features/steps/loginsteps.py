from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_impl(context):
    serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
    context.driver = webdriver.Chrome(service=serv_obj)


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.NAME, "txtUsername").send_keys(user)
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)


@when('Click on the login button')
def step_impl(context):
    context.driver.find_element(By.ID, "btnLogin").click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
