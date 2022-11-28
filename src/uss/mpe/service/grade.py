"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
이순신 90 90 92 272 90.6 A
유관순 90 90 92 272 90.6 A
********************************
"""

class Grade(object):
    def __init__(self,name,ko,en,ma): #여기에는 입력받는 인스턴스값을 꼭 적어줘야.
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma



    def get_total(self):
        self. total = self.ko + self.en + self.ma
        return self.total

    def get_avg(self):
        return self.get_total() / 3

    def get_grade(self):
        avg = self.get_avg()
        if avg >= 90:
            grade ="A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade ="C"
        elif avg >= 60:
            grade ="D"
        elif avg >= 50:
            grade ="E"
        else:
            grade ="F"
        return grade

    def execute(self):
        self.get_total()
        self.get_avg()
        self.get_grade()


    def __str__(self):
        return f"{self.name} {self.ko} {self.en} {self.ma} {self.get_total()} {self.get_avg()} {self.get_grade()}"

    @staticmethod
    def print_menu():
        print("1. 성적 등록")
        print("2. 성적 출력")
        print("3. 성적 삭제")
        print("4. 종료")
        menu = int(input("메뉴 선택: "))
        return int(menu)

    @staticmethod
    def new_grade():
        name = input("이름: ")
        ko = int(input("국어: "))
        en = int(input("영어: "))
        ma = int(input("수학: "))
        return Grade(name,ko,en,ma)


    @staticmethod
    def print_grades(ls):
        print("### 성적표 ###")
        print("********************************")
        print("이름 국어 영어 수학 총점 평균 학점")
        print("********************************")
        [print(i) for i in ls]
        print("********************************")

    @staticmethod
    def delect_grade(ls,name):
        '''for i,j in enumerate(ls):
            if j.name == name:
                del ls[i]'''
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]] #인덱스와 엘레멘트의 리스트에서 엘레멘트의 이름이 입력한 이름 값과 같으면 그 인덱스를 선택됨.[0]는 그 인덱스의 첫번째라는 의미


