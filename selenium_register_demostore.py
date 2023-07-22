'''
This selenium script will verify the email registration process in the ecommerce store
The script can only be run once since an error will be generated once an email used
for registration already exists in the database.

Created By - Jeniffer Lagman
Date - July 20, 2023

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import random
import string

driver = webdriver.Chrome()

driver.get('http://localhost:8888/mysite1/my-account/')

# find the email field
user_email = driver.find_element(By.ID, 'reg_email')

# assert email field is enabled
# assert user_email.is_enabled(), "The user email field is not displayed."

if not user_email.is_displayed():
    raise Exception("The user email field is not displayed.")

# generate a random string composed of 10 characters
letters = string.ascii_letters
random_string = ''.join(random.sample(letters, 10))

# get today's date
today = date.today()

# concatenate the random string, datetime and email domain to generate email
email = random_string + today.strftime("%Y%m%d_%H%M%S") + "@gmail.com"

# input email into the field
user_email.send_keys(email)

# find the password field
user_pwd = driver.find_element(By.ID, 'reg_password')

# assert password field is enabled

if not user_pwd.is_displayed():
    raise Exception("The password field is not displayed.")

# input the password into the field
user_pwd.send_keys('AT#CDsdfadf98!')

# click on the Register button
register_btn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')
register_btn.click()

print("Email has been registered successfully.")
print("PASS")


''' Raise an error message if account/email address already exists in the system
error_msg_elem = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li' )

displayed_txt = error_msg_elem.text

expected_txt = 'Error: An account is already registered with your email address. Please log in.'

if displayed_txt == expected_txt:
    raise Exception("Email address already exists. FAIL.")
'''









