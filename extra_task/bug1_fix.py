"""
Find the bugs and fix this script with Python and Selenium
​
Test case:
    Open Wikipedia org
    Search for Python
    Verify Python is on the results
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = "https://www.wikipedia.org/"
browser.get(url)

search_bar = browser.find_element(By.CSS_SELECTOR, "input.searchInput")
search_query = "python"
search_bar.clear()
search_bar.send_keys(search_query)

assert search_query in browser.current_url, f"Search query {search_query} not in {browser.current_url}"
print("Test case passed")

browser.close()
