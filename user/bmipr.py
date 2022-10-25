from util.common import Common


class Bmi(object):
    def __init__(self, name, kg, cm):
        self.name = name
        self.kg = kg
        self.cm = cm

    def get_bmi(self):
        kg = self.kg
        m = self.cm / 100
        return kg / m ** 2

    def get_biman(self):
        bmi = self.get_bmi()
        if bmi >= 35:
            biman = "고도비만"
        elif bmi >= 30:
            biman = "중도비만"
        elif bmi >= 25:
            biman = "경도비만"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "고도비만"
        else:
            biman = "저체중"
        return biman

    def __str__(self): # str을 쓰면 마지막이 프린트하는걸로 바뀜.
        return f"{self.name} {self.kg} {self.cm} {self.get_biman()}"

    @staticmethod
    def new_bmi():
        name = input("이름: ")
        cm = int(input("키: "))
        kg = int(input("몸무게: "))
        return Bmi(name, cm, kg)

    @staticmethod
    def prints(ls):
        [print(i) for i in ls]

    @staticmethod
    def delect(ls,name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]



