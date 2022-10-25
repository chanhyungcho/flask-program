"""
이름, 주민번호 (950101-1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.

출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25세 (만나이)
성별: 남성
주소: 서울
********************************
"""
from util.common import Common

class Person(object):
    def __init__(self,name,ssn,add):
        self.name = name
        self.ssn = ssn
        self.add = add


    def get_gender(self):
        gender_checker = int(self.ssn[7])
        if gender_checker == 1 or gender_checker == 2:
           if gender_checker == 1:
               self.gender = "남성"
           else:
               self.gender = "여성"
        if gender_checker == 3 or gender_checker ==4:
            if gender_checker == 3:
                self.gender = "남성"
            else:
                self.gender = "여성"
        return self.gender


    def get_age(self):
        current = 2022  # ssn[:2]는 출생년도 ex) 90.. 00
        gender_checker = int(self.ssn[7])
        year = int(self.ssn[:2])
        if gender_checker == 1 or gender_checker == 2:
            year += 1900
        if gender_checker == 3 or gender_checker == 4:
            year += 2000
        return current - year


    def print_info(self):
        print(f"이름:{self.name}")
        print(f"나이:{self.get_age()}")
        print(f"성별:{self.get_gender()}")
        print(f"주소:{self.add}")
        print("*"*20)

    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        return int(input("메뉴:"))

    @staticmethod
    def new_pr():
        name = input("이름: ")
        ssn = input("주민번호: ")
        add = input("주소: ")
        return Person(name,ssn,add)

    @staticmethod
    def print_pr(ls):
        print("### 자기소개어플 ###")
        print("********************************")
        [i.print_info() for i in ls]
        print("********************************")

    @staticmethod
    def delect_pr(ls,name):
    #    for i,j in enumerate(ls):
    #        if j.name == name:
    #            del ls[i]
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]




