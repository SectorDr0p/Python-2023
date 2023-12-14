import sys
import requests
from pprint import pprint

inp = sys.argv[1]
url = f"https://restcountries.com/v3.1/name/{inp}?fullText=true"
response = requests.request(method="GET", url=url)


print()
print(25*"*")
print()
print(response.json()[0]['name'])
print(25*"*")
data = response.json()[0]
pprint(data.keys())
print(f'Ludnosc:\t{data["population"]}')
print(f'Powierzchnia:\t{data["area"]}')
print(f'Waluta:\t\t{list(data["currencies"].keys())[0]}')
print(f'Stolica:\t{data["capital"]}')
