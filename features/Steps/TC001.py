from behave import *   # bdd dilini import ettik
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage


@given(u'I got navigated to Home Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")






@when(u'I enter')
def step_impl(context):
    home_page=HomePage(context.driver)
    home_page.click_on_my_account()  #butona tiklama methodu olusturmustuk , direk onu cagirdik



@when(u'kkkk')
def step_impl(context):
    pass  # ptyhon da simdilik birsey yapma, adimi gecir gibi



@then(u'lllll')
def step_impl(context):
    expected_test="bu yazi gorunsun"
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed
    



@given(u'I aaaaaa')
def step_impl(context):
    pass



@when(u'I nterxxxxx')
def step_impl(context):
    pass


@when(u'kkxxxx')
def step_impl(context):
    pass



@then(u'lllvvvvv')
def step_impl(context):
    pass

