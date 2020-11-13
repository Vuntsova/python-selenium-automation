from behave import given,when,then
from selenium.webdriver.common.by import By


@when('Click Orders')
def orders(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-orders"]/span[2]').click()


@then('Verify Sign In Page opens')
def verify_action(context):
    url = context.driver.current_url;
    assert 'signin?' in url
    assert 'Sign-In' in context.driver.find_element(By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div['
                                                              '1]/form/div/div/div/h1').text
