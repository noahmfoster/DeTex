import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def walk_pages(alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    links = []
    for letter in alphabet:
        url = f"https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Mathematics/List_of_mathematics_articles_({letter})"
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Error on {letter}: Status code', response.status_code)
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links += [link['href'] for link in soup.find(id="bodyContent").find_all('a') if link['href'].startswith('/wiki/')]
    return links

def get_equations(url, prefix = "https://en.wikipedia.org"):
    response = requests.get(prefix + url)
    if response.status_code != 200:
        print('Error: Status code', response.status_code)
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_title = soup.find('title').text
    equations = soup.find_all('img', class_='mwe-math-fallback-image-inline')
    print('Found', len(equations), 'equations on', page_title)
    if len(equations) > 0:
        return (page_title, [equation['alt'] for equation in equations])
    else:
        return []

if __name__ == '__main__':
    links = walk_pages()
    print('Found', len(links), 'links')

    # url = "https://en.wikipedia.org/wiki/Pythagorean_theorem"
    # equations = get_equations(url)
    # print(equations)