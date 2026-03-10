#!/usr/bin/env python3
"""
HK Laws - find correct URL pattern from index
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

# Get the chapter index page
url = "https://www.elegislation.gov.hk/index/chapternumber"
print(f"Loading: {url}")
driver.get(url)
time.sleep(5)

# Find links to laws
links = driver.find_elements(By.TAG_NAME, "a")
law_links = []

for link in links:
    try:
        href = link.get_attribute("href") or ""
        text = link.text.strip()
        if "cap" in href.lower() and text:
            law_links.append((text, href))
    except:
        pass

print(f"Found {len(law_links)} law links")
for text, href in law_links[:20]:
    print(f"  {text}: {href}")

driver.quit()
