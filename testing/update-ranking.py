from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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
time.sleep(4)
 
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
time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='root']/div[1]/main/div/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[4]/span/label[3]/span[1]").click()

time.sleep(4)