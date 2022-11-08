#from scrapper.domains import MusicRanking
from scrapper.domains import Scrap
from scrapper.views import ScrapController
from util.common import Common

if __name__ == '__main__':
    api = ScrapController()
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
            api.menu_1(scrap)
        elif menu == "2":
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
            scrap.query_string = "2022110811"
            scrap.parser = "lxml"
            scrap.class_names = ["ellipsis rank01", "ellipsis rank02"]
            scrap.tag_name = "div"
            api.menu_2(scrap)
        else:
            print("잘못된 선택입니다")