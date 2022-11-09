MENUS = ["종료",
         "메타데이터 출력",
         "poptotal/popasian 변수를 total/asian로 이름변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]

def key(ls):
        for i,j in enumerate(ls):
                print(f"{i} {j}")
                return input(f"메뉴: ")

class Midwest:
    pass

if __name__ == '__main__':
    while True:
        key = key(MENUS)
        pass
