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
print(greeting.text)
if greeting.text == "Hello, Sign in":
    print("greeting.text")
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]/span[1]')).perform()
    driver.find_element(By.XPATH, '//*[@id="nav-flyout-ya-signin"]/a/span').click()

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
