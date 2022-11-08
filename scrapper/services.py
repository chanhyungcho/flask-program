from future.backports import urllib
import urllib.request as urllib

from bs4 import BeautifulSoup


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