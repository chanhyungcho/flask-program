import googlemaps
import numpy as np
import openpyxl
import pandas as pd
from scipy import stats
from sklearn.preprocessing import OrdinalEncoder

from sklearn.model_selection import train_test_split

CRIME_MENUS = ["종료",#0
         "spec",#1
         "merge",#2. 여러개의 데이터프레임을 하나로 통합
         "Interval",#3
         "Norminal",#4
         "Target",#5
         "Partition",#6
         "readexcel" #7
         "Fit",
         "Predict"]



crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.interval(),
    "4" : lambda t: t.nominal(),
    "5" : lambda t: t.target_id(),
    "6" : lambda t: t.partition(),
    "7" : lambda t: t.call_xls(),
}






class CrimeService:
    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.pop = pd.read_excel('./data/pop_in_seoul.xls')
        self.ls = [self.crime,self.cctv,self.pop]
        print(pd.read_excel('./data/pop_in_seoul.xls', usecols=[1, 3, 6, 9, 13], skiprows=[0,2]))



    '''
    1.스펙보기
    '''

    # 값에 대한 정의가 안되서 람다? #람다는 식 하나 밖에 할당안됨.
    def temp(self):
        """return lambda x:print(
                (" --- 1.Shape ---"),
                (x.shape)
                (" --- 2.Features ---"),
                (x.columns)
                (" --- 3.Info ---"),
                (x.info())
                (" --- 4.Case Top1 ---"),
                (x.head(1))
                (" --- 5.Case Bottom1 ---"),
                (x.tail(3))
                (" --- 6.Describe ---"),
                (x.describe())
                (" --- 7.Describe All ---"),
                (x.describe(include='all')))"""







    def spec(self):
        print("클로저테스트")
        #__init__ 이 아님. 속성값을 만들지 않음(메모리를 점유하지 않음). s는 지역변수?로 기능을 가짐.(주소만 가짐. 실행만 하고 사라짐).

        [(lambda x: print(f"--- 1.Shape ---\n{x.shape}\n"
                               f"--- 2.Features ---\n{x.columns}\n"
                               f"--- 3.Info ---\n{x.info}\n"
                               f"--- 4.Case Top1 ---\n{x.head(1)}\n"
                               f"--- 5.Case Bottom1 ---\n{x.tail(3)}\n"
                               f"--- 6.Describe ---\n{x.describe()}\n"
                               f"--- 7.Describe All ---\n{x.describe(include='all')}"))
        (i) for i in self.ls]



    def save_police_pos(self):
        crime = self.crime
        station_names =[]
        for name in crime['관서명']:
            print(f"지역이름: {name}")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f"서울시내 경찰서는 총 {len(station_names)}개 이다.")
        [print(f"{str(i)}") for i in station_names]

        gmaps = (lambda x: googlemaps.Client(key=x))("")
        print(gmaps.geocode("서울중부경찰서", language='ko'))
        print("API에서 주소 추출 시작")
        station_addrs=[]
        station_lats=[]
        station_lngs=[]
        for i,name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lat'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv('./save/police_pos.csv',index=False)


    '''
    3. 이산형
    '''

    def interva(self): #숫자 자체. 구간변수.
        pass


    def ratio(self): # 비율
        pass

    '''4.범주형'''

    def nominal(self): #순서가 없는
        pass

    def ordinal(self): # 순서가 있는
        pass

    '''
        5. 타깃변수(=종속변수 dependent, Y값) 설정
        입력변수(=설명변수, 확률변수, X값)
        타깃변수명: stroke (=뇌졸중)
        타깃변수값: 과거에 한번이라도 뇌졸중이 발병했으면 1, 아니면 0
    '''

    def target_id(self):
        df = pd.read_csv('./save/2017DC1.csv')
        self.data = df.drop(['주택가격중위수'], axis=1)
        self.target = df['주택가격중위수']
        print(self.data.shape)
        print(self.target.shape)

    '''
    6.파티션
    '''

    def partition(self):
        self.target_id()
        X_train, X_test, y_train, y_test = train_test_split(self.data, self.target, test_size=0.5,
                                                            random_state=42)
        print('X_train shape:', X_train.shape)
        print('X_test shape:', X_test.shape)
        print('y_train shape:', y_train.shape)
        print('y_test shape:', y_test.shape)
        return X_test




if __name__ == '__main__':
    c = CrimeService()
    c.spec()