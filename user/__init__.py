from user.contact import Contact
from user.grade import Grade
from user.person import Person
from util.common import Common
from user.bmipr import Bmi

ls = []
while True:
    menu = Common.menu(["Bmi", "주소록", "성적표", "개인정보", "종료"])
    if menu == 0:
        submenu = Common.menu(["Bmi 등록", "Bmi 목록", "Bmi 삭제", "종료"])
        if submenu == 0:
            print("###bmi 등록###")
            ls.append(Bmi.new_bmi())
        elif submenu == 1:
            print("###bmi 목록###")
            Bmi.prints(ls)
        elif submenu == 2:
            print("###bmi 삭제###")
            Bmi.delect(ls, input("삭제할 이름:"))
        elif submenu == 3:
            print("###종료###")
            break
        else:
            print("다시 선택하십시오")
    elif menu ==1:
        print("주소록")
        submenu = Common.menu(["연락처 등록", "연락처 출력", "연락처 삭제", "종료"])
        if submenu == 0:
            print("###연락처 등록###")
            ls.append(Contact.new_contact())  # 덧붙이다, 첨부하다 / [ ]에 추가할 때는 append
        elif submenu == 1:
            print("###연락처 출력###")
            Contact.get_contacts(ls)
        elif submenu == 2:
            print("###연락처 삭제###")
            Contact.delect_contact(ls, input("삭제할 이름"))
        elif submenu == 3:
            print(" 주소록 어플을 종료합니다...")
            break
        else:
            print("다시 선택하십시오")
    elif menu == 2:
        print("성적표")
        submenu = Common.menu(["## 성적 등록 ##", "## 성적 출력 ##","## 성적 삭제 ##", "## 종료 ##"])
        if submenu == 0:
            print("## 성적 등록 ##")
            ls.append(Grade.new_grade())
        elif submenu == 1:
            print("## 성적 출력 ##")
            Grade.print_grades(ls)
        elif submenu == 2:
            print("## 성적 삭제 ##")
            Grade.delect_grade(ls, input("삭제할 이름: "))
        elif submenu == 3:
            print("## 종료 ##")
            break
        else:
            print("잘못된 선택입니다.")
    elif menu == 3:
        print("개인정보")
        submenu = Common.menu(["## 명부 등록##", "## 명부 출력##", "## 명부 삭제##", "## 종료##"])
        if submenu == 0:
            print("## 명부 등록##")
            ls.append(Person.new_pr())
        elif submenu == 1:
            print("## 명부 출력##")
            Person.print_pr(ls)
        elif submenu == 2:
            print("## 명부 삭제##")
            Person.delect_pr(ls, input("삭제할 이름:"))
        elif submenu == 3:
            print("## 종료##")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하십시오.")
    elif menu == 4:
        print("종료")
        break
    else:
        print("다시 선택하십시오")

