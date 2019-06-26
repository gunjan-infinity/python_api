import requests
import json
mac_address = str(input("Enter Mac Address"));
url = 'https://api.macaddress.io/v1?apiKey=at_TR6ryG2tv3MGKatdEgidOLZJhM32d&output=json&search='+mac_address
r = requests.get(url)
data = json.loads(r.content.decode())
print(data['vendorDetails']['companyName'])