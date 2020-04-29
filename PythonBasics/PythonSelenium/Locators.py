from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Ankit")
# css
driver.find_element_by_css_selector("input[name='name']").send_keys("Ankit")

driver.find_element_by_name("email").send_keys("ankitptrivedi@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("abc123def")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)

# xpath
driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text #CSS
# xpath -> //*[contains(@class,'alert-success')]
assert "Success" in message


