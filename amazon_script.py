from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# init driver
driver = webdriver.Chrome('/Users/emiliya/Desktop/automation_cource/Lesson_1/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

greeting = driver.find_element(By.XPATH, '//span[text()="Hello, Sign in"]')

if greeting.text == "Hello, Sign in":

    hover = ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]/span[1]'))
    hover.perform()

    sign_in = driver.find_element(By.XPATH, '//*[@id="nav-flyout-ya-signin"]/a/span')
    sign_in.click()

    sign_in_email = driver.find_element(By.ID, 'ap_email')
    sign_in_email.clear()
    sign_in_email.send_keys('vuntsova@aol.com')

    sign_in_continue = driver.find_element(By.ID, "continue")
    sign_in_continue.click()

    sign_in_password = driver.find_element(By.ID, 'ap_password')
    sign_in_password.clear()
    sign_in_password.send_keys('123123Ee')

    sign_in_submit = driver.find_element(By.ID, "signInSubmit")
    sign_in_submit.click()

    verification_required = driver.find_element(By.XPATH, '//*[@id="auth-mfa-form"]/div/div/h1')
    print(verification_required.text)
    # verify
    assert 'Two-Step Verification' in verification_required.text
else:
    driver.quit()
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Dress')

# wait for 4 sec
sleep(4)

# click search
# driver.find_element(By.NAME, 'btnK').click()

# verify
# assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
# assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()
