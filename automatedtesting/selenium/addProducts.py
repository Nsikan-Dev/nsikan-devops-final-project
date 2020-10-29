# #!/usr/bin/env python
from selenium import webdriver
import time

# Start the browser and navigate to https://www.saucedemo.com/inventory.html.
print('Navigating to https://www.saucedemo.com/inventory.html')
print('Adding all items to cart')
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/inventory.html')
driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
print('Adding backpack to cart')
driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
print('Adding bike light to cart')
driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
print('Adding t-shirt to cart')
driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
print('Adding fleece jacket to cart')
driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
print('Adding onesie to cart')
driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
print('Adding t-shirt to cart')

time.sleep(5)

print('Removing all items from cart')
driver.find_element_by_css_selector("button[class='btn_secondary btn_inventory']").click()
driver.find_element_by_css_selector("button[class='btn_secondary btn_inventory']").click()
driver.find_element_by_css_selector("button[class='btn_secondary btn_inventory']").click()
driver.find_element_by_css_selector("button[class='btn_secondary btn_inventory']").click()
driver.find_element_by_css_selector("button[class='btn_secondary btn_inventory']").click()
driver.find_element_by_css_selector("button[class='btn_secondary btn_inventory']").click()

print('Done')
