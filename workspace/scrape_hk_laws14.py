#!/usr/bin/env python3
"""
HK Laws - find PDF download link using Selenium properly
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-plugins")

driver = webdriver.Chrome(options=chrome_options)

# Go to a law page
url = "https://www.elegislation.gov.hk/hk/cap1"
print(f"Loading: {url}")
driver.get(url)
time.sleep(10)

# Print URL and title
print(f"URL: {driver.current_url}")
print(f"Title: {driver.title}")

# Look for any link containing "pdf"
links = driver.find_elements(By.TAG_NAME, "a")
pdf_links = []

for link in links:
    try:
        href = link.get_attribute("href") or ""
        text = link.text.strip()
        if "pdf" in href.lower() or "pdf" in text.lower():
            pdf_links.append((text, href))
    except:
        pass

print(f"\nFound {len(pdf_links)} PDF links")
for text, href in pdf_links[:10]:
    print(f"  {text}: {href}")

# Try to find any download-related elements
print("\n\nLooking for download button...")
buttons = driver.find_elements(By.TAG_NAME, "button")
for btn in buttons:
    try:
        text = btn.text.strip()
        onclick = btn.get_attribute("onclick") or ""
        if text or onclick:
            print(f"  Button: {text} | {onclick[:50]}")
    except:
        pass

# Check for any element with data attributes
print("\n\nLooking for elements with data attributes...")
elems = driver.find_elements(By.CSS_SELECTOR, "[data-download], [data-pdf], [data-export]")
for elem in elems:
    try:
        print(f"  {elem.tag_name}: {elem.get_attribute('outerHTML')[:100]}")
    except:
        pass

driver.quit()
