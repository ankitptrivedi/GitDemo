import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_css_selector("div[class='product']"))
# count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for b in buttons:
    b.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
time.sleep(4)
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# driver.find_element_by_xpath("//div[@class='cart-preview active']/div[2]/button").click()

# driver.find_element_by_css_selector("input[class='promoCode']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
# time.sleep(5)
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
# time.sleep(7)
driver.find_element_by_xpath("//button[text()='Place Order']").click()

