'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
### 비만도 계산 ###
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
'''


class Bmi(object):
    new_bmi = None

    def __init__(self,name,kg,cm):
        self.name = name
        self.kg = kg
        self.cm = cm
        self.bmi = 0
        self.biman =""

    def get_bmi(self):
        kg = self.kg
        m = self.cm / 100
        self.bmi = kg / m**2

    def get_biman(self):
        biman = self.bmi
        if biman >= 35:
            result = "고도비만"
        elif biman >= 30:
            result = "중도비만"
        elif biman >= 25:
            result = "경도비만"
        elif biman >= 23:
            result ="과체중"
        elif biman >= 18.5:
            result ="고도비만"
        else:
            result ="저체중"
        return result


    def execute(self):
        self.get_bmi()
        self.get_biman()

    def print_info(self):
        print(f"{self.name}, {self.cm}, {self.kg}, {self.get_biman()}")

    @staticmethod
    def print_menu():
        print("1. 비만 등록")
        print("2. 비만 출력")
        print("3. 비만 삭제")
        print("4. 종료")
        menu = int(input("메뉴 선택: "))
        return int(menu)

    @staticmethod
    def new_bmi():
        name = input("이름: ")
        kg = int(input("몸무게: "))
        cm = int(input("키: "))
        return Bmi(name,kg,cm)

    @staticmethod
    def get_bmi(ls):
        print("### 비만도 계산 ###")
        print("***************************")
        print("### 이름 키(cm) 몸무게(kg) 비만도 ###")
        print("***************************")
        [i.print_info() for i in ls]
        print("***************************")

    @staticmethod
    def delect_bmi(ls,name):
        '''for i,j in enumerate(ls):
            if j.name == name:
                del ls[i]'''
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def main():
        ls=[]
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print("##1.BMI 등록##")
                ls.append(Bmi.new_bmi())
            elif menu == 2:
                print("##2.BMI 출력##")
                Bmi.get_bmi(ls)
            elif menu == 3:
                print("##1.BMI 삭제##")
                Bmi.delect_bmi(ls,input("이름: "))
            elif menu == 4:
                print("##4. 종료##")
                break
            else:
                print("잘못된 선택입니다.")


Bmi.main()