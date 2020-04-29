from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("This is an automated test")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
