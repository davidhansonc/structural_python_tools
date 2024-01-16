import requests
from bs4 import BeautifulSoup
import os
import urllib.request

shapes = "W shapes"
url = "https://www.cad-steel.com/steel-sections/c-shapes-american-standard-channels"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')  # assuming the data is in the first table

links = table.find_all('a')

base_url = "https://www.cad-steel.com"

# Create a directory for the files
dir_name = os.path.join(os.path.expanduser('~'), 'Desktop', shapes)
os.makedirs(dir_name, exist_ok=True)

for link in links:
    file_url = base_url + link.get('href')
    file_name = os.path.join(dir_name, link.text + ".dwg")  # assuming the files are in .dwg format
    urllib.request.urlretrieve(file_url, file_name)
    print(f"Downloaded {file_name}")