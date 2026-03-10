#!/usr/bin/env python3
"""
HK Laws - check network requests and find content
"""
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Enable network logging
caps = DesiredCapabilities.CHROME
caps["goog:loggingPrefs"] = {"performance": "ALL"}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=chrome_options, desired_capabilities=caps)

url = "https://www.elegislation.gov.hk/chi/cap1.html"
driver.get(url)
time.sleep(10)

# Get logs (network requests)
logs = driver.get_log("performance")
print("Network requests:")
for log in logs[:30]:
    try:
        msg = json.loads(log["message"])
        if "request" in msg.get("message", {}):
            req = msg["message"]["request"]
            url = req.get("url", "")
            if "pdf" in url.lower() or "export" in url.lower() or "download" in url.lower():
                print(f"  {req.get('method')} {url}")
    except:
        pass

# Also check for API calls
print("\n\nAll network requests with JSON:")
for log in logs[:50]:
    try:
        msg = json.loads(log["message"])
        if "request" in msg.get("message", {}):
            req = msg["message"]["request"]
            url = req.get("url", "")
            if "api" in url.lower() or "json" in url.lower():
                print(f"  {req.get('method')} {url}")
    except:
        pass

driver.quit()
