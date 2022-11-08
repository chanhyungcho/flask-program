from dataclasses import dataclass
import urllib.request
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from const.path import CTX


'''지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.'''
'''
class BugsMusic:
    def __init__(self,url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        title = {"class":"title"}
        artist = {"class":"artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        [print(f"{i}위{j.find('a').text}: {e.find('a').text}")
         for i, j, e in zip(range(1,len(titles)), titles, artists)]

class Melon:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urlopen(urllib.request.Request(self.url, headers=self.headers))
        soup = BeautifulSoup(req, 'lxml')
        title = {"class":"rank01"}
        artist = {"class":"rank02"}
        titles = soup.find_all(name="div", attrs=title)
        artists = soup.find_all(name="div", attrs=artist)
        [print (f"{i}위{j.find('a').text} {e.find('a').text}")
         for i,j,e in zip(range(1,len(titles)),titles,artists)]
'''
@dataclass
class Scrap:

    html = ''
    parser= ''
    domain= ''
    query_string = ''
    headers= {}
    tag_name = ''
    fname = ''
    class_names= []
    artists= []
    titles= []
    diction= {}
    df = None
    soup = BeautifulSoup

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = './save/result.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)
