#!/usr/bin/env python3
"""
HK Laws - check the redirect
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=chrome_options)

# Try direct URL
url = "https://www.elegislation.gov.hk/chi/cap1.html"
print(f"Navigating to: {url}")
driver.get(url)
time.sleep(5)
print(f"After get - URL: {driver.current_url}")
print(f"Title: {driver.title}")

# Check if we need to add parameters
url_with_params = "https://www.elegislation.gov.hk/chi/cap1.html?JS_FN=1&searchword=*"
print(f"\nNavigating to: {url_with_params}")
driver.get(url_with_params)
time.sleep(5)
print(f"After get - URL: {driver.current_url}")
print(f"Title: {driver.title}")

# Print some page content
print(f"\nPage text sample: {driver.page_source[5000:8000]}")

driver.quit()
