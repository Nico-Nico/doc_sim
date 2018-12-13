import requests
from bs4 import BeautifulSoup
response = requests.get(my_url)
soup = BeautifulSoup(response.text)
soup.find(id="intro-text")
# Result:
<p id="intro-text">No javascript support</p>