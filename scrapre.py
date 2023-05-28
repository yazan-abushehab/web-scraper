import requests
from bs4 import BeautifulSoup
import json

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count (url):
    page = requests.get(URL)
    # print (page)
    # print (page.content)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print (soup)

    all_head = soup.find_all('sup',class_='noprint')
    # print (all_head)
    return len(all_head)

print(get_citations_needed_count(URL))

def get_citations_needed_report(url):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_paragraph = soup.find_all('p')
    para_list = []
    for s in all_paragraph:  
            if s.find('sup',class_='noprint'):
                   para_list.append(s.text)  

    string = '\n'.join(para_list)
    return string

print(get_citations_needed_report(URL))    

    