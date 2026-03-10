#!/usr/bin/env python3
"""
HK Laws - try different URL patterns
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

# Try different URL patterns
urls = [
    "https://www.elegislation.gov.hk/chi/cap1.html",
    "https://www.elegislation.gov.hk/chi/cap1",
    "https://www.elegislation.gov.hk/chi/cap001.html",
    "https://www.elegislation.gov.hk/chi/cap1.htm",
    "https://www.elegislation.gov.hk/hk/cap1.html",
    "https://www.elegislation.gov.hk/eng/cap1.html",
]

for url in urls:
    print(f"\n=== {url} ===")
    driver.get(url)
    time.sleep(5)
    print(f"URL: {driver.current_url}")
    print(f"Title: {driver.title[:50]}")

driver.quit()
