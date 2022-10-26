class Common(object):
    def __init__(self):
        pass

    @staticmethod
    def menu(ls):
        #ls = ["등록", "출력", "삭제", "종료"]
        for i,j in enumerate(ls):
            print(f"{i} {j}")
        return input("메뉴 선택: ")


    '''@staticmethod
    def menu():
        print ("0.등록")
        print ("1.출력")
        print ("2.삭제")
        print ("3.종료")
        menu = int(input("메뉴"))
        return menu'''

