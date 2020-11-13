from behave import given, when, then
from selenium.webdriver.common.by import By

WEBSITE = 'https://www.amazon.com/gp/help/customer/display.html'
HELP_SEARCH_FIELD = (By.ID, 'helpsearch')
GO_BUTTON = ()
TITLE = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[3]/div/div/h1')


# Actions


@given('Go to Amazon Help Page')
def open_help_page(context):
    context.driver.get(WEBSITE)


@when('Use “Search the help library” field and search for Cancel order')
def search_in_help(context):
    search_cancel_order = context.driver.find_element(*HELP_SEARCH_FIELD)
    search_cancel_order.send_keys('Cancel Order')


@when('Click Go button')
def search_in_help(context):
    context.driver.find_element(*HELP_SEARCH_FIELD).click()


@then('Verify that ‘Cancel Items or Orders’ text is present')
def verify_search(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=hp_search_rd_gw?__mk_en_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&help_keywords=cancel+order&search=true&nodeId=508510&kwHidden=true&sprefix=cancle+or%2Ccancel+order%2C1&locale=en_US')
    search_title = context.driver.find_element(*TITLE)
    assert "Cancel Items or Orders" in search_title.text
