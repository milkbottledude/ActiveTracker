import pandas as pd
from bs4 import BeautifulSoup
import csv
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = r'https://crowdcapacity.net/'

driver_service = Service(executable_path=r"C:\Users\Yu Zen\Documents\Coding\chromedriver-win64\chromedriver.exe")
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Set user agent
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
#chrome_options.add_argument("window-size=1920x1080")  # Set window size
#chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
csv_filepath = r"C:\Users\Yu Zen\Documents\Coding\Project-activetrack\data.csv"

def scrapegood(url):
    driver = webdriver.Chrome(service=driver_service)
    driver.get(url)
    driver.implicitly_wait(2)
    lines = driver.find_elements(By.CSS_SELECTOR,"span[style='display: flex; align-items: center; justify-content: center;']")
    # names = driver.find_elements(By.CSS_SELECTOR, "p[class='text-base md:text-3xl my-2 md:my-4']")
    # nem = ['datetime']
    # for name in names:
    #     nem.append(name.text)
    timestamp = datetime.now().strftime("%Y-%m-%d %A %H:%M")
    new_row = [timestamp]
    for line in lines:
        new_row.append(line.text)
    driver.quit()
    df = pd.read_csv('data.csv')
    # Append the new row using loc
    df.loc[len(df)] = new_row
    df.to_csv('data.csv', index=False)
    print(new_row)


    # with open(csv_filepath, mode='a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow((new_row))

print(scrapegood(url))



