from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import time

DRIVER_PATH = "/usr/local/bin/chromedriver"

with open("creds.txt") as f:
        uname = f.readline()
        pwrd = f.readline()
            

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

# wait for login to happen
time.sleep(4)

