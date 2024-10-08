from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re

""""
This file contains a testing script used for HTML DOM scraping written in Python.
The script uses the Selenium library to open a Chrome browser and navigate to a LinkedIn profile page.
It then uses the BeautifulSoup library to extract the HTML of the page and parse it to extract the profile information.
"""

DRIVER_PATH = "/usr/local/bin/chromedriver"

# extracting credentials from txt file on my pc
with open("pwrd.txt") as f:
    email = f.readline()
    pwrd = f.readline()

# Configure web driver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
 
# waiting for the page to load
time.sleep(4)
 
# entering username
username = driver.find_element(By.ID, "username")
 
# Enter Your Email Address
username.send_keys(str(email)) 
 
# entering password
pword = driver.find_element(By.ID, "password")
# In case of an error, try changing the element
# tag used here.
 
# Enter Your Password
pword.send_keys(str(pwrd))       

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
time.sleep(3)

# Opening Demo Profile
profile_url = "https://www.linkedin.com/in/bassmit1/"
my_network = "https://www.linkedin.com/mynetwork/"
 
#driver.get(my_network)
#time.sleep(4)

driver.get(profile_url)        # this will open the link
time.sleep(1)

# Scroll to bottom of profile page
start = time.time() 
initialScroll = 0
finalScroll = 1000
 
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
 
    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(3)
 
    end = time.time()
    # Scroll for 20 seconds
    if round(end - start) > 10:
        break

# Extracting data from profile
src = driver.page_source
soup = BeautifulSoup(src, "html.parser")

# Extracting the HTML of the complete introduction box
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
 
html_pattern = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
#print(re.sub(html_pattern, '', str(intro)))

# Extracting the Name
name_loc = intro.find("h1")
name = name_loc.get_text().strip()

# Extracting the description underneath Name
description_loc = intro.find('div', {'class': 'text-body-medium'})
description = description_loc.get_text().strip()
 
# Extracting the Location
location_loc = soup.find('div', { 'class': 'pv-text-details__left-panel mt2'})
location = location_loc.get_text().strip()
 
# printing the extracted data
print("Name: ", name,
      "\nDescription: ", description,
      "\nLocation: ", location)

