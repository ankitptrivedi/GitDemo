from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.familysearch.org/en/")
action = ActionChains(driver)

action.move_to_element(driver.find_element_by_css_selector("button[aria-controls='search']")).click().perform()
# nav_bar = driver.find_element_by_css_selector("button[aria-controls='search']")
# action.move_to_element(nav_bar).click().perform()

# action.move_to_element(driver.find_element_by_id("search")).perform()
# action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()
driver.find_element_by_link_text("Genealogies").click()


