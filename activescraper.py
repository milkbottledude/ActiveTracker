import pandas as pd
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver_service = Service(executable_path=r"C:\Users\Yu Zen\Documents\Coding\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

url = r'https://crowdcapacity.net/'
driver.get(url)
driver.implicitly_wait(10)
driver.quit()