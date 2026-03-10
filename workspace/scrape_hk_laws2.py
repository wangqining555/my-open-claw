#!/usr/bin/env python3
"""
HK Laws Scraper - try different approach
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=chrome_options)

OUTPUT_DIR = "/root/.openclaw/workspace/hk-laws-pdf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_page_and_download(cap_num, lang="chi"):
    """Get the law page and try to find PDF link"""
    url = f"https://www.elegislation.gov.hk/{lang}/cap{cap_num}.html"
    print(f"\n=== Cap {cap_num} ({lang}) ===")
    print(f"URL: {url}")
    
    driver.get(url)
    time.sleep(3)
    
    # Get page source to see what's there
    page_source = driver.page_source[:500]
    print(f"Page starts with: {page_source[:200]}")
    
    # Look for PDF links
    try:
        pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
        print(f"Found {len(pdf_links)} PDF links")
        for link in pdf_links[:5]:
            href = link.get_attribute("href")
            text = link.text
            print(f"  {text}: {href}")
    except Exception as e:
        print(f"Error finding PDF links: {e}")
    
    # Also try to find download buttons
    try:
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Found {len(buttons)} buttons")
        for btn in buttons[:5]:
            text = btn.text
            onclick = btn.get_attribute("onclick") or ""
            print(f"  Button: {text} -> {onclick[:100]}")
    except Exception as e:
        print(f"Error finding buttons: {e}")

# Try a few chapters
for cap in [1, 2, 210]:
    get_page_and_download(cap, "chi")

driver.quit()
print("\nDone!")
