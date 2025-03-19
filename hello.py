from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www2.1010data.com/prime-17.35/")

time.sleep(5)

driver.quit()