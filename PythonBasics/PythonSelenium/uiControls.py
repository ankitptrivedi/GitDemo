from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

check = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(check))

for c in check:
    if c.get_attribute("value") == "option2":
        c.click()
        assert c.is_selected()

but = driver.find_elements_by_xpath("//input[@type='radio']")

print(len(check))

but[2].click()
assert but[2].is_selected()

msg = driver.find_element_by_id("displayed-text").is_displayed()
print(msg)
assert msg

driver.find_element_by_id("hide-textbox").click()
msg1 = driver.find_element_by_id("displayed-text").is_displayed()

assert not msg1
