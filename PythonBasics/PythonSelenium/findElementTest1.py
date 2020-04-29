import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com")

driver.find_element_by_id('fromCity').click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("vancouver")
time.sleep(2)
results = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(results))
for res in results:
    if res.text == 'Vancouver, Canada':
        res.click()
        break

#
# driver.find_element_by_css_selector("input[placeholder='To']").send_keys('toronto')
# time.sleep(2)
# # driver.find_element_by_css_selector("input[placeholder='To']").send_keys("toro")
driver.find_element_by_xpath("//p[text()='Delhi, India']").click()

# driver.find_element_by_id("toCity").click()
# # driver.find_element_by_css_selector("input[placeholder='To']").send_keys("del")
# driver.find_element_by_xpath()
# results1 = driver.find_elements_by_css_selector("p[class*='blackText']")
#
# for res1 in results1:
#     if res1.text == 'Delhi, India':
#         res1.click()
