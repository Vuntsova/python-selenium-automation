from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

WEBSITE = 'https://www.amazon.com/'
GREETING_MESSAGE = (By.XPATH, '//span[text()="Hello, Sign in"]')
ACCOUNT_AND_LISTS = (By.XPATH, '//*[@id="nav-link-accountList"]/span[1]')
SIGN_BUTTON = (By.XPATH, '//*[@id="nav-flyout-ya-signin"]/a/span')
EMAIL_INPUT = (By.ID, 'ap_email')
TEST_EMAIL_CREDENTIALS = 'vuntsova@aol.com'
CONTINUE_BUTTON = (By.ID, "continue")
PASSWORD_INPUT = (By.ID, 'ap_password')
TEST_PASSWORD_CREDENTIALS = '123123Ee'
SUBMIT_BUTTON = (By.ID, "signInSubmit")
VERIFICATION_REQUIRED = (By.XPATH, '//*[@id="auth-mfa-form"]/div/div/h1')


@given('Open the Amazon Page')
def open_amazon(context):
    context.driver.get(WEBSITE)


@when('Check If Logged In')
def login(context):
    greeting = context.driver.find_element(*GREETING_MESSAGE)

    if greeting.text == "Hello, Sign in":
        pass
    else:
        context.sleep(4)
        context.driver.quit()


@when('Hover over Account & List')
def hover(context):
    hover_it = ActionChains(context.driver).move_to_element(context.driver.find_element(*ACCOUNT_AND_LISTS))
    hover_it.perform()


@when('Click the Sign In button')
def sign(context):
    sign_in_button = context.driver.find_element(*SIGN_BUTTON)
    sign_in_button.click()


@when('Enter Email Address in the input field')
def email(context):
    sign_in_email = context.driver.find_element(*EMAIL_INPUT)
    sign_in_email.clear()
    sign_in_email.send_keys(TEST_EMAIL_CREDENTIALS)


@when('Click Continue Button')
def continue_to_login(context):
    sign_in_continue = context.driver.find_element(*CONTINUE_BUTTON)
    sign_in_continue.click()


@when('Enter Password in the input field')
def password(context):
    sign_in_password = context.driver.find_element(*PASSWORD_INPUT)
    sign_in_password.clear()
    sign_in_password.send_keys(TEST_PASSWORD_CREDENTIALS)


@when('Click Sign In button')
def sign_in(context):
    sign_in_submit = context.driver.find_element(*SUBMIT_BUTTON)
    sign_in_submit.click()


@then('Verification Code Is Required')
def verify(context):
    verification_required = context.driver.find_element(*VERIFICATION_REQUIRED)
    assert 'Two-Step Verification' in verification_required.text

    sleep(2)
