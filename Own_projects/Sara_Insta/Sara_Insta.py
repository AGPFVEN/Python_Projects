from requests import get
from bs4 import BeautifulSoup

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/61.0.3163.100 Safari/537.36'}

insta_url = 'https://www.instagram.com/saraabasolo/'
response = get(insta_url, headers=usr_agent)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
result_block = soup.find_all('div', {'class': 'v1Nh3 kIKUG  _bz0w'})
print(soup)
print(result_block)