from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.yatra.com")
driver.find_element_by_id("BE_flight_origin_city").click()
driver.find_element_by_css_selector("input[class='required_field cityPadRight ac_input origin_ac']").send_keys("del")
results = driver.find_elements_by_css_selector("p[class='ac_cityname']")

for res in results:
    if res.text == "Del Rio":
        res.click()
