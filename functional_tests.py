"""Just One Thing functional testing module"""

# standard library imports


# pip installed
from selenium import webdriver

# app modules


browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title