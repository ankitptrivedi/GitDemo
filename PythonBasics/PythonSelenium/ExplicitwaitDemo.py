import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
list2 = []
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_css_selector("div[class='product']"))
# count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4
for b in buttons:
    list.append(b.find_element_by_xpath("parent::div/parent::div/h4").text)
    b.click()

print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
veggies = driver.find_elements_by_css_selector("p.product-name")
for v in veggies:
  list2.append(v.text)
print(list2)

assert list == list2

# Code to grab amount before applying the discount
org_amt = driver.find_element_by_css_selector('.discountAmt').text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

# Code to grab amount after applying the discount
disc_amt = driver.find_element_by_css_selector('.discountAmt').text

assert float(disc_amt) < int(org_amt)

print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_elements_by_xpath('//tr/td[5]/p')
sum = 0
for a in amounts:
    sum = sum + int(a.text)

print(sum)
tot_amt = int(driver.find_element_by_css_selector('.totAmt').text)

assert sum == tot_amt

# driver.find_element_by_xpath("//button[text()='Place Order']").click()
