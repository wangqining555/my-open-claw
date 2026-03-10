#!/usr/bin/env python3
"""
HK Laws - get the actual law content from page
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.elegislation.gov.hk/chi/cap1.html"
driver.get(url)
time.sleep(10)

# Get page title and some content
print(f"Title: {driver.title}")
print(f"URL: {driver.current_url}")

# Try to find the main content area
# Look for common content container IDs
content_selectors = [
    "#content", "#main", "#bodyContent", ".content", 
    "main", ".main", "article", ".body"
]

for sel in content_selectors:
    try:
        elem = driver.find_element(By.CSS_SELECTOR, sel)
        print(f"\n{sel}: {elem.text[:500]}")
    except:
        pass

# Let's also check for any element containing "第" (Chinese for "Article")
try:
    elems = driver.find_elements(By.XPATH, "//*[contains(text(), '第')]")
    print(f"\n\nElements with '第': {len(elems)}")
    if elems:
        print(f"First one: {elems[0].text[:200]}")
except Exception as e:
    print(f"Error: {e}")

driver.quit()
