import hashlib
import io
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

username = "901295"

# initialize the Chrome driver
driver = webdriver.Chrome()

# head to login page
driver.get("https://shop.app4sales.net/jollein/#catalog?filter=B23BC445B3C4B451016878C5464AACF7")

# wait for the page to load
wait = WebDriverWait(driver, 30)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-bind="value: username"][required]')))

# find username/email field and send the username itself to the input field
username_input = driver.find_element(By.CSS_SELECTOR, 'input[data-bind="value: username"][required]')
username_input.send_keys(username)

# after manually entering the password, click login button
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-bind="click: onAuthenticate"]')
login_button.click()

# create a BeautifulSoup object from the page content
SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')
