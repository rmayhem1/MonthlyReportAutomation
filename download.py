import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Load environment variables
load_dotenv()

WEBSITE_URL = os.getenv("WEBSITE_URL")
USERNAME = os.getenv("WEBSITE_USERNAME")
PASSWORD = os.getenv("WEBSITE_PASSWORD")

# Setup Firefox options
options = webdriver.FirefoxOptions()
# options.add_argument("--headless")  # run without opening a visible window

print("Setting up Firefox...")
service = FirefoxService(GeckoDriverManager().install())

print("Opening Firefox browser...")
driver = webdriver.Firefox(service=service, options=options)

print(f"Navigating to {WEBSITE_URL}...")
driver.get(WEBSITE_URL)

print("Page loaded successfully")

# Keep window open for 10 seconds to see it
time.sleep(5)

# Close the window
print("Closing browser...")
driver.quit()



