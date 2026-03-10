#!/usr/bin/env python3
"""
HK Laws - try clicking on HTML view and then PDF
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
time.sleep(8)

# Look for "HTML" or "PDF" text links
links = driver.find_elements(By.TAG_NAME, "a")
print("All links with text:")
for link in links:
    try:
        text = link.text.strip()
        href = link.get_attribute("href") or ""
        if text and len(text) < 30:
            print(f"  [{text}]: {href[:80]}")
    except:
        pass

# Try to find specific links - maybe with certain patterns
print("\n\nLooking for 'html' or 'pdf' in link text:")
for link in links:
    try:
        text = link.text.strip().lower()
        href = link.get_attribute("href") or ""
        if 'html' in text or 'pdf' in text:
            print(f"  [{link.text.strip()}]: {href}")
    except:
        pass

driver.quit()
