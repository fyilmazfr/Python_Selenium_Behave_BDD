from behave import *

@given("I open the application")
def step_open_application(context):
    print("Application opened")

@when('I enter username "{username}"')
def step_enter_username(context, username):
    print(f"Username entered: {username}")

@when('I enter password "{password}"')
def step_enter_password(context, password):
    print(f"Password entered: {password}")

@when("I click on login button")
def step_click_login(context):
    print("Clicked login button")

@then('I should see the message "{message}"')
def step_verify_message(context, message):
    print(f"Expected message: {message}")
