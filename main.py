from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv() #import .env file contents

username = os.getenv("USERINFO")
password = os.getenv("PASSWORD")
url = os.getenv("URL")

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5) #wait until elements are loaded on page (CHANGE TO WebDriverWait in future)

#grab login/password login boxes via XPATH
username_field = driver.find_element(By.XPATH, '//*[@id="uid"]') 
password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div[2]/form/div[4]/input') #had to use full XPATH bc shortened was not working

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.XPATH, '//*[@id="submit_button"]')
login_button.click()

#add long wait (WebDriver Explicit Wait) here bc login times are atrocious

