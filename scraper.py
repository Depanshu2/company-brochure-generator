from bs4 import BeautifulSoup
import requests

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def website_content(url):
    """
     here we will extract the contents from a wesbite 
    """

    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    
    title=soup.title.string if soup.title else ""

    if soup.body:
        for irrelevant in soup.body(['script','img','style','input']):
            irrelevant.decompose()
        text=soup.body.get_text(separator='\n',strip=True)
    else:
        text=""

    return (title + "\n\n" + text)[:3000]


def relevant_links(url):

    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')

    links=[link.get('href') for link in soup.find_all('a')]
    return links