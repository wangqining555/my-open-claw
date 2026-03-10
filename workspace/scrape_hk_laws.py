#!/usr/bin/env python3
"""
Hong Kong Laws Scraper using Selenium + Chromium
"""
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

# Create driver
driver = webdriver.Chrome(options=chrome_options)

# Output directory
OUTPUT_DIR = "/root/.openclaw/workspace/hk-laws-pdf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_law_list():
    """Get list of all law chapter numbers"""
    # Try to access the main page and get law list
    url = "https://www.elegislation.gov.hk/"
    print(f"Loading {url}...")
    driver.get(url)
    time.sleep(3)
    
    # Try to find chapter index
    try:
        # Look for chapter number index link
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href") or ""
            text = link.text or ""
            if "chapternumber" in href.lower() or "index" in href.lower():
                print(f"Found: {text} -> {href}")
    except Exception as e:
        print(f"Error finding links: {e}")
    
    # Since we can't easily navigate, let's try direct download URLs
    # The format should be something like /chi/capXXX.pdf
    return list(range(1, 601))  # Try caps 1-600

def download_law(cap_num, lang="chi"):
    """Download a single law PDF"""
    url = f"https://www.elegislation.gov.hk/{lang}/cap{cap_num}.pdf"
    
    # Get the page first to set cookies
    driver.get(url)
    time.sleep(1)
    
    # Check if download happened or if we got HTML
    current_url = driver.current_url
    print(f"Cap {cap_num} ({lang}): {current_url}")
    
    # If it's not a PDF, try to find PDF link on page
    if "html" in current_url.lower() or "www.elegislation.gov.hk/chi/cap" in current_url:
        try:
            # Look for PDF link
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href") or ""
                if href.endswith(".pdf"):
                    print(f"  Found PDF link: {href}")
                    # Download it
                    return download_pdf(href, cap_num, lang)
        except:
            pass
    
    return False

def download_pdf(url, cap_num, lang):
    """Download PDF from URL using requests with session cookies"""
    try:
        # Get cookies from selenium
        cookies = driver.get_cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        
        # Download with same headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://www.elegislation.gov.hk/',
        }
        
        r = session.get(url, headers=headers, timeout=30)
        
        if r.status_code == 200 and b'%PDF' in r.content[:20]:
            filepath = os.path.join(OUTPUT_DIR, f"cap{cap_num}_{lang}.pdf")
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"  Saved: {filepath} ({len(r.content)} bytes)")
            return True
        else:
            print(f"  Failed: status={r.status_code}, size={len(r.content)}")
            return False
    except Exception as e:
        print(f"  Error: {e}")
        return False

# Main
print("Starting HK Laws scraper...")
chapters = get_law_list()
print(f"Found {len(chapters)} chapters to download")

# Try a few first
for cap in [1, 2, 3, 50, 100]:
    print(f"\n=== Trying cap {cap} ===")
    download_law(cap, "chi")

driver.quit()
print("\nDone!")
