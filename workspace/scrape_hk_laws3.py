#!/usr/bin/env python3
"""
HK Laws Scraper - look for all links
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

def get_all_links(cap_num, lang="chi"):
    url = f"https://www.elegislation.gov.hk/{lang}/cap{cap_num}.html"
    print(f"\n=== Cap {cap_num} ({lang}) ===")
    
    driver.get(url)
    time.sleep(5)  # Wait for JS to fully load
    
    # Get ALL links
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Total links: {len(links)}")
    
    # Print all links with href
    for link in links:
        href = link.get_attribute("href") or ""
        text = link.text.strip()[:30]
        if href:
            print(f"  [{text}]: {href}")

# Try cap 1
get_all_links(1, "chi")

driver.quit()
