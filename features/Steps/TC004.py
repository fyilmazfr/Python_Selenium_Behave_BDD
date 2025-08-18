from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



@given('I open the Google home page')   #bu adimi silebiliriz before after methodu yaptik
def step_impl(context):

    time.sleep(1)

@when('I search for "{query}"')
def step_impl(context, query):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

@then('I should see results related to "{query}"')
def step_impl(context, query):
    assert query.lower() in context.driver.page_source.lower()
    context.driver.quit()
