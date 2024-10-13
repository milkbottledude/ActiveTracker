from google.cloud import storage
from io import StringIO
import pandas as pd

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
    # to be continued
    print('scraping successful')
    return df


def returndata(updateddf):
    buffer = io.StringIO()
    updateddf.to_csv(buffer, index=False)
    blob.upload_from_string(buffer.getvalue(), content_type='text/csv')
    print('returned to sender')