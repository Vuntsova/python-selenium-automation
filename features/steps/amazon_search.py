from behave import given, when, then
from selenium.webdriver.common.by import By

WEBSITE = 'https://www.amazon.com/'
SEARCH_INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.XPATH, '//*[@id="nav-search-submit-text"]/input')
SEARCH_RESULT = (By.XPATH, '//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[3]')


@given('Open Amazon Page Now')
def open_site(context):
    context.driver.get(WEBSITE)


@when('Input Dress')
def input_search_word(context):
    context.driver.find_element(*SEARCH_INPUT_FIELD).send_keys('Dress')


@when('Click on Amazon search button')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_BUTTON).click()


@then('Search result Dress')
def verify_search_results(context):
    result = context.driver.find_element(*SEARCH_RESULT)
    assert result.text == '"Dress"', f'Error.Expected Dress, bot got {result.text}'
