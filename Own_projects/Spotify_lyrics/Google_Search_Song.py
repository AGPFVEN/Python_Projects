from requests import get
from bs4 import BeautifulSoup

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/61.0.3163.100 Safari/537.36'}
                      
def Search_lyrics(name_artists, name_song):
    formatted_name_artists = name_artists.replace(',', '')
    print('{} {} lyrics'.format(formatted_name_artists, name_song))
    search_term = '{} {} lyrics'.format(formatted_name_artists, name_song)
    escaped_search_term = search_term.replace(' ', '+')

    google_url = 'https://www.google.com/search?q={}'.format(escaped_search_term)
    print(google_url)
    response = get(google_url, headers=usr_agent)
    response.raise_for_status()
    # print(response.text)

    return response.text

def Parse_Lyrics(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    result_block = list(soup.find_all('span', attrs={'jsname': 'YS01Ge'}))
    print(result_block)
    for verse in result_block:
        unformatted_verse = str(verse).replace('<span jsname="YS01Ge">', '')
        formatted_verse = unformatted_verse.replace('</span>', '')
        print(formatted_verse)
        yield verse

def Show_Lyrics(name_artists, name_song):
    list(Parse_Lyrics(Search_lyrics(name_artists, name_song)))