from selenium import webdriver
text = 'Ankit'
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/AutomationPractice")

# driver.find_element_by_id("input[id='name']").click()
driver.find_element_by_css_selector("#name").send_keys(text)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
assert text in alert.text
alert.accept()

driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
alert.dismiss()
