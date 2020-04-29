from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://chercher.tech/practice/popups")

actions = ActionChains(driver)

actions.move_to_element(driver.find_element_by_id("double-click")).double_click().perform()
alert = driver.switch_to.alert

print(alert.text)
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
