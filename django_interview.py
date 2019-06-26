#import pandas as pd
import requests
import json

# def scatter_chart():
#     dataset = pd.read_csv('media/sample_superstore.csv',encoding ='latin1')
#     df = pd.DataFrame(dataset)
#     df = df[['Region','Sales']]
#     new_dataset = df.groupby('Region')['Sales']
#     print(df)
#
# scatter_chart()
#
# def column_chart():
#     dataset = pd.read_csv('media/sample_superstore.csv',encoding = 'latin1')
#     df = pd.DataFrame(dataset)


mac_address = str(input())
url = 'https://api.macaddress.io/v1?apiKey=at_TR6ryG2tv3MGKatdEgidOLZJhM32d&output=json&search='+mac_address
r = requests.get(url)
data = json.loads(r.content.decode())
print(data['vendorDetails']['companyName'])
