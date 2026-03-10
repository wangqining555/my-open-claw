#!/usr/bin/env python3
"""
HK Laws - get raw page source
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

url = "https://www.elegislation.gov.hk/chi/cap1.html"
driver.get(url)
time.sleep(8)  # Wait longer

# Get page source
html = driver.page_source

# Print parts that might contain PDF links
import re
# Find all hrefs
hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
pdf_hrefs = [h for h in hrefs if '.pdf' in h.lower()]
print(f"PDF hrefs found: {len(pdf_hrefs)}")
for h in pdf_hrefs[:20]:
    print(f"  {h}")

# Also look for JavaScript that might generate PDF
js_matches = re.findall(r'javascript:[^"\']+', html)
print(f"\nJS patterns: {len(js_matches)}")
for j in js_matches[:10]:
    print(f"  {j[:100]}")

driver.quit()
