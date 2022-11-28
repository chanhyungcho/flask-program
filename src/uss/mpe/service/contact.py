'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인원은 여러명 저장 가능합니다.
'''

class Contact(object):
    def __init__(self,name,pnum,email,add) -> None:
        self.name = name
        self.pnum = pnum
        self.email = email
        self.add = add

    @staticmethod
    def new_contact():
        name = input("이름:")
        pnum = input("전화번호:")
        email = input("이메일:")
        add = input("주소:")
        return Contact(name,pnum,email,add)

    def __str__(self):
         return f"{self.name}, {self.pnum}, {self.email}, {self.add}"

    @staticmethod
    def get_contacts(ls):
        [print(i) for i in ls]

    @staticmethod
    def delect_contact(ls, name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]


    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = int(input("메뉴 선택: "))
        return int(menu)

