#!/usr/bin/env python3
"""
HK Laws Scraper - check page for PDF download section
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

def analyze_page(cap_num, lang="chi"):
    url = f"https://www.elegislation.gov.hk/{lang}/cap{cap_num}.html"
    print(f"\n=== Cap {cap_num} ({lang}) ===")
    
    driver.get(url)
    time.sleep(5)
    
    # Try to find element by ID or class that might contain download options
    # Look for common download patterns
    elements = driver.find_elements(By.CSS_SELECTOR, "*")
    
    # Look for elements with 'download', 'pdf', 'export' in id/class/text
    for elem in elements[:200]:  # Check first 200
        try:
            elem_id = elem.get_attribute("id") or ""
            elem_class = elem.get_attribute("class") or ""
            elem_text = elem.text.strip()[:30]
            elem_tag = elem.tag_name
            
            if any(x in elem_id.lower() + elem_class.lower() + elem_text.lower() for x in ['download', 'pdf', 'export', 'print', 'html']):
                print(f"{elem_tag} [id={elem_id[:20]} class={elem_class[:20]}]: {elem_text}")
        except:
            pass
    
    # Try getting page source to see if PDF URL is hidden somewhere
    html = driver.page_source
    
    # Look for PDF-related strings in HTML
    if ".pdf" in html.lower():
        import re
        pdf_matches = re.findall(r'href=["\']([^"\']*\.pdf[^"\']*)["\']', html, re.I)
        print(f"\nPDF links in HTML: {pdf_matches[:10]}")

# Try cap 1
analyze_page(1, "chi")

driver.quit()
