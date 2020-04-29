from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
# chrome_options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
# driver.find_element_by_xpath("//a[text()='Blackberry']")
allProducts = driver.find_elements_by_xpath("//div[@class='card h-100']")

products = []
for product in allProducts:
    prodName = product.find_element_by_xpath("div/h4/a").text
    products.append(prodName)
    if prodName == "Nokia Edge":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

prodName1 = driver.find_element_by_xpath("//h4[@class='media-heading']/a").text
print(prodName1)
print(products)

assert prodName1 in products

driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
successMsg = driver.find_element_by_css_selector('.alert-success').text

assert 'Success!' in successMsg

driver.get_screenshot_as_file("img.png")
