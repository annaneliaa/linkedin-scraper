from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
import time

DRIVER_PATH = "/usr/local/bin/chromedriver"

uname = "ff-admin"
pwrd = "Ipsec@22"

# Configure web driver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Opening Finding Founders login page
driver.get("https://ff.slimmerai.dev/")

# waiting for the page to load
time.sleep(10)
 
username = driver.find_element(By.NAME, "username")

username.send_keys(str(uname)) 

# entering password
pword = driver.find_element(By.NAME, "password")

# Enter Your Password
pword.send_keys(str(pwrd))      

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

# wait for login to happen & page to load
time.sleep(10)

driver.find_element(By.XPATH, "//button[@title='Messages']").click()

# wait for sidebar to load
time.sleep(10)

# click on "Add Message" button
button = driver.find_element(By.XPATH, "//*[contains(text(), 'Add Message')]").click()

# get input box that appears
input_box = driver.find_element(By.CLASS_NAME, "EmptyMessage")

# click to start typing
input_box.sendKeys(Keys.TAB)

time.sleep(2)

# send message and save
input_box.clear()
input_box.send_keys("Hello, this is a test message from Selenium!")
input_box.send_keys(Keys.ENTER)

time.sleep(10)