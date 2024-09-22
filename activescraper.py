import pandas as pd
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
driver_service = Service(executable_path=r"C:\Users\Yu Zen\Documents\Coding\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

url = r'https://crowdcapacity.net/'
driver.get(url)
driver.implicitly_wait(2)
lines = driver.find_elements(By.CSS_SELECTOR,"span[style='display: flex; align-items: center; justify-content: center;'][class='badge-light badge bg-success sgds']")
yishuncap = lines[-2].text
timestamp = datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")
to_add = pd.DataFrame({timestamp: [yishuncap]})
to_add = to_add.T
to_add.to_csv(r"/home/milkbottledude/Project-activetrack/data.csv", mode='a', header=False, index=True)
driver.quit()



