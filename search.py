from bs4 import BeautifulSoup
import urllib.request
import spacy
import re
import random
from spacy.lang.es.examples import sentences



def get_links(url):
    try:
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")
    except:
        return "HTTP not finded"
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    wikisAUX = []
    for link in links:
        wikisAUX.append(extract_name(link))

    wikis = []
    for i in range(len(wikisAUX)):
        if wikisAUX[i] is not None:
            wikis.append(wikisAUX[i])

    names = get_names(wikis)
    links_name = []
    for name in names:
        name = name.replace(" ","_")
        link_main = "https://en.wikipedia.org/wiki/" + name
        if link_main != "https://en.wikipedia.org/wiki/Privacy_policy" or link_main != "https://en.wikipedia.org/wiki/Main_Page":
            if link_main.count("_") <= 2:
                links_name.append(link_main)
    

    name_actual = extract_name(url)
    return ((name_actual, url), links_name)

def search(tuple):
    r = random.randint(3,len(tuple[1])-1)
    return get_links(tuple[1][r])



    

def check_soup(url):
    try:
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")
        return soup
    except:
        return ""

def extract_name(link):
    if link is not None:
        pattern = r'wiki/(\w+)'
        matches = re.findall(pattern,link)
        if len(matches) >= 1:
            name = matches[0].replace("_"," ")
            return name

def get_names(wikis):
    names = []
    nlp = spacy.load("es_core_news_sm")
    for i in wikis:
        doc = nlp(i)
        for ent in doc.ents:
            if ent.label_ == "PER":
                names.append(i)
    names = list(dict.fromkeys(names))
    return names


