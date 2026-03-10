#!/usr/bin/env python3
"""
HK Laws - check network requests and find content
"""
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.elegislation.gov.hk/chi/cap1.html"
driver.get(url)
time.sleep(10)

# Get logs (network requests)
logs = driver.get_log("performance")
print("Network requests with pdf/export:")
for log in logs:
    try:
        msg = json.loads(log["message"])
        if "request" in msg.get("message", {}):
            req = msg["message"]["request"]
            url = req.get("url", "")
            if any(x in url.lower() for x in ["pdf", "export", "download", "api"]):
                print(f"  {req.get('method')} {url[:150]}")
    except:
        pass

driver.quit()
