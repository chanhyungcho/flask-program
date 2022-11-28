from future.backports import urllib
import urllib.request as urllib
import os
from bs4 import BeautifulSoup

from dataclasses import dataclass
import urllib.request
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from src.cmm.const.path import CTX, static
#from scrapper.domains import MusicRanking


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
        path =  f'{static}/save/cop/scp/melon_ranking.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)


def BugsMusic(arg):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.Request(arg.domain + arg.query_string, headers=headers)
    a = urllib.urlopen(req)
    b = a.read().decode('utf-8')
    soup = BeautifulSoup(b, arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]

    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]

    diction = {} # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장


def Melon(arg):
    # soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.Request(arg.domain + arg.query_string, headers=headers)
    a = urllib.urlopen(req)
    b = a.read().decode('utf-8')
    soup = BeautifulSoup(b, arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)


    [print(f"{i}위 {j.find('a').text} : {k.find('a').text}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]


    diction = {}
    print("#"*10)
    print(len(titles))
    for i,j in zip(titles, artists):
        diction[j.find('a').text] = i.find('a').text
    print(diction)
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장




if __name__ == '__main__':

    scrap = Scrap()
    while True:
        menu = input("0:종료, 1:벅스:, 2:멜론:")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names = ["title", "artist"]
            scrap.tag_name = "p"
            BugsMusic(scrap)
        elif menu == "2":
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
            scrap.query_string = "2022110811"
            scrap.parser = "lxml"
            scrap.class_names = ["ellipsis rank01", "ellipsis rank02"]
            scrap.tag_name = "div"
            Melon(scrap)
        else:
            print("잘못된 선택입니다")
            
'''
@dataclass
class ScrapVO:
    html = ''
    parser = ''
    domain = ''
    query_string = ''
    headers = {}
    tag_name = ''
    fname = ''
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = f'{static}/save/cop/scp/melon_ranking.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)

def BugsMusic(arg):

    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    diction = {} # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장


def MelonMusic(arg):
    soup = BeautifulSoup(urlopen(urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent' : "Mozilla/5.0"})), "lxml")
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    diction = {} # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장

music_menus = ["Exit", #0
                "BugsMusic",#1
                "MelonMusic",#2.
                ]
if __name__=="__main__":
    scrap = ScrapVO()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(music_menus)]
        menu = input('메뉴선택: ')
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("벅스")
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names=["title", "artist"]
            scrap.tag_name = "p"
            BugsMusic(scrap)
        elif menu == "2":
            print("멜론")
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
            scrap.query_string = "2022110909"
            scrap.parser = "lxml"
            scrap.class_names = ["rank01", "rank02"]
            scrap.tag_name = "div"
            MelonMusic(scrap)
        elif menu == "3":
            df = pd.read_csv(f"{static}/save/cop/scp/bugs_ranking.csv")
            print(df)
        else:
            print("해당메뉴 없음")
