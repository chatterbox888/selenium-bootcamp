'''
This script will input an invalid coupon code once an item has been checked out from the cart.
An error message will be displayed.

Created by - Jeniffer Lagman
Date - July 20, 2023

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Webdriver
driver = webdriver.Chrome()

# Navigate to the cart page
# driver.get('http://bootcamp.store.supersqa.com/')
driver.get("http://localhost:8888/mysite1/")


# Search for an item to be added to the cart and click on it
item = driver.find_element(By.CSS_SELECTOR, '#main > ul > li.product.type-product.post-24.status-publish.instock.product_cat-music.has-post-thumbnail.downloadable.virtual.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
item.click()

time.sleep(2)

# Go to the cart
driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a').click()

coupon_field = driver.find_element(By.ID, 'coupon_code')
# coupon_field = driver.find_element(By.CSS_SELECTOR, '#coupon_code')

# Enter an invalid coupon code
coupon_field.send_keys("TEST")

# Click on the Apply button
apply_btn = driver.find_element(By.CSS_SELECTOR, '#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
apply_btn.click()
time.sleep(3)

# Display an error message when an invalid coupon code is inputted
error_msg_elem = driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul/li' )

displayed_txt = error_msg_elem.text

expected_txt = 'Coupon "test" does not exist!'

if displayed_txt != expected_txt:
    raise Exception("Invalid coupon code message."
                    f"Expected: {expected_txt}. Actual:{displayed_txt}")
else:
    print("Invalid coupon code.")

print("PASS")


# Close the browser
driver.quit()