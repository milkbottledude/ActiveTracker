from google.cloud import storage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from io import StringIO
import pandas as pd
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Sets user agent



url = r'https://crowdcapacity.net/'

BUCKET_NAME = 'frickubucket'
data = 'data.csv'

def getdata(bucketname):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucketname)
    blob = bucket.blob(data)
    with blob.open('r') as resume_file:
        df = pd.read_csv(io.StringIO(resume_file.read()))
    return df

def scraping(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(2)
    lines = driver.find_elements(By.CSS_SELECTOR,"span[style='display: flex; align-items: center; justify-content: center;']")
    timestamp = datetime.now().strftime("%Y-%m-%d %A %H:%M")
    new_row = [timestamp]
    for line in lines:
        new_row.append(line.text)
    driver.quit()
    # to be continued
    print('scraping successful')
    return new_row


def returndata(df, new_row):
    df.loc[len(df)] = new_row
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    blob.upload_from_string(buffer.getvalue(), content_type='text/csv')
    print('returned to sender')

def main():
    getdata(BUCKET_NAME)
    scraping(url)
    returndata(getdata, scraping)
    print('all done :)')

if __name__ == '__main__':
    main()