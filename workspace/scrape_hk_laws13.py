#!/usr/bin/env python3
"""
HK Laws - Full scraper with correct URLs
"""
import os
import time
import requests
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

OUTPUT_DIR = "/root/.openclaw/workspace/hk-laws-pdf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_all_laws():
    """Get all law URLs from index"""
    url = "https://www.elegislation.gov.hk/index/chapternumber"
    driver.get(url)
    time.sleep(5)
    
    links = driver.find_elements(By.TAG_NAME, "a")
    laws = []
    
    for link in links:
        try:
            href = link.get_attribute("href") or ""
            text = link.text.strip()
            if "hk/cap" in href and text and "cap" in href.lower():
                laws.append((text, href))
        except:
            pass
    
    return laws

def try_download_pdf(law_url, law_name):
    """Try to download PDF from law page"""
    # Navigate to law page
    driver.get(law_url)
    time.sleep(3)
    
    # Try to find PDF link or get current URL
    current = driver.current_url
    
    # Check if there's PDF format available
    # Try adding /pdf to URL
    pdf_url = law_url + ".pdf"
    
    # Use requests to check if PDF exists (faster)
    try:
        r = requests.head(pdf_url, timeout=10, allow_redirects=True)
        if r.status_code == 200 and "pdf" in r.headers.get("content-type", ""):
            # Download it
            r = requests.get(pdf_url, timeout=30)
            filename = law_url.split("/cap")[-1] + ".pdf"
            filepath = os.path.join(OUTPUT_DIR, filename)
            with open(filepath, "wb") as f:
                f.write(r.content)
            print(f"Saved: {filename} ({len(r.content)} bytes)")
            return True
    except Exception as e:
        pass
    
    return False

# Get all laws
print("Getting law list...")
laws = get_all_laws()
print(f"Found {len(laws)} laws")

# Try to download first 10 as test
print("\nTrying to download PDFs...")
for i, (name, url) in enumerate(laws[:10]):
    print(f"{i+1}. {name[:50]}: {url}")
    try_download_pdf(url, name)

driver.quit()
print("\nDone!")
