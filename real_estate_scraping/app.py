import requests
from bs4 import BeautifulSoup

url = "https://www.century21.com"
r = requests.get("")
c = r.content

soup = BeautifulSoup(c, "html.parser")
