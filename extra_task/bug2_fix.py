"""
Find the bugs and fix this script with Python and Selenium
​
WWrite different locators for the search bar and the button
​
The following import can't be used:
from selenium.webdriver.common.keys import Keys
​
Test case:
    Open google.com
    Search for Python
    Verify Python is on the results
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="")

url = "https://www.google.com"
browser.get(url)

search_bar = browser.find_element(By.CSS_SELECTOR, "input.gLFyf")
search_query = "python"
search_bar.clear()
search_bar.send_keys(search_query)

browser.find_element(By.CSS_SELECTOR, "input.gNO89b").click()

assert search_query == browser.current_url, f"Search query {search_query} not in {browser.current_url}"
print("Test case passed")

browser.close()