import time
import os
import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.google.com/')

if response.status_code == 200:
    print("good connection")
elif response.status_code == 404:
    print("Bad gateway")
time.sleep(1)

print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify)
#link for the parser of the stockprice- 
#https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN




