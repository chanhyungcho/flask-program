import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split

STROKE_MENUS = ["종료",#0
         "데이터구하기",#1
         "변수한글화",#2
         "연속형변수편집",#3
         "범주형변수편집",#4
         "샘플링",#5
         "모델링",
         "학습",
         "예측"]

stroke_meta = {
    'id' : '아이디',
    'gender' : '성별',
    'age' : '나이',
    'hypertension': '고혈압',
    'heart_disease' : '심장병',
    'ever_married' : '기혼여부',
    'work_type' :  '근무형태',
    'Residence_type' : '주거형태',
    'avg_glucose_level' : '평균혈당',
    'bmi' : '체질량지수',
    'smoking_status' : '흡연여부',
    'stroke' : '뇌졸중'
}

stroke_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.nominal_variables(),
    "5" : lambda t: t.sampling(),
    "6" : lambda t: t.find_highest_hwy(),
    "7" : lambda t: t.which_cty_in_suv_compact(),
    "8" : lambda t: t.find_top5_hwy_in_audi(),
    "9" : lambda t: t.find_top3_avg(),
}


'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''




class StrokeService:
    def __init__(self):
        self.adult_stroke = None
        self.storke = pd.read_csv('../../../../static/data/dam/ml/healthcare.csv')
        self.my_storke = None

    '''
       1.스펙보기
       '''

    def spec(self):
        print(" --- 1.Shape ---")
        print(self.storke.shape)
        print(" --- 2.Features ---")
        print(self.storke.columns)
        print(" --- 3.Info ---")
        print(self.storke.info())
        print(" --- 4.Case Top1 ---")
        print(self.storke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.storke.tail(3))
        print(" --- 6.Describe ---")
        print(self.storke.describe())
        print(" --- 7.Describe All ---")
        print(self.storke.describe(include='all'))

    '''
    2.한글 메타데이터
    '''

    def rename_meta(self):
        self.my_storke = self.storke.rename(columns=stroke_meta)
        print(" --- 2.Features ---")
        print(self.my_storke.columns)



    '''
    3. 타깃변수(=종속변수 dependent, Y값) 설정
    입력변수(=설명변수, 확률변수, X값)
    타깃변수명: stroke (=뇌졸중)
    타깃변수값: 과거에 한번이라도 뇌졸중이 발병했으면 1, 아니면 0
    '''

    def ratio_variables(self): # 해당 컬럼이 없음
        pass

    def interval_variables(self):
        df = self.my_storke
        interval = ['나이', '평균혈당', '체질량지수']
        pd.options.display.float_format = '{:.2f}'.format
        df[interval].describe()
        c=df['나이'] > 18
        self.adult_stroke=df[c]
        print(f'-----성인객체스펙-----\n{self.adult_stroke.shape}')
        t=self.adult_stroke
        c1 = t['평균혈당'] <=232.64
        c2 = t['체질량지수'] <=60.3
        self.adult_stroke = t[c1 & c2]
        print(f'-----이상치 제거한 성인객체스펙-----\n{self.adult_stroke.shape}')


    '''
    4.범주형 = ['성별','심장병','기혼여부','근무형태',
                   '주거형태','흡연여부','고혈압',]
    '''

    def nominal_variables(self):
        t = self.adult_stroke
        category = ['성별','심장병','기혼여부','근무형태',
                   '주거형태','흡연여부','고혈압']
        print(f'범주형 변수 데이터타입\n {t[category].dtypes}')
        print(f'범주형 변수 결측값\n {t[category].isnull().sum()}')
        print(f'결측값 가진 변수 유무\n {t[category].isna().any()[lambda x:x]}')
        t['성별'] = OrdinalEncoder().fit_transform(t['성별'].values.reshape(-1,1))
        t['기혼여부'] = OrdinalEncoder().fit_transform(t['기혼여부'].values.reshape(-1,1))
        t['주거형태'] = OrdinalEncoder().fit_transform(t['주거형태'].values.reshape(-1,1))
        t['흡연여부'] = OrdinalEncoder().fit_transform(t['흡연여부'].values.reshape(-1,1))
        self.storke =t
        self.spec()
        print('###finish preprocess')
        self.storke.to_csv("./save/stroke.csv")

    def ordinal_variables(self): # 해당 컬럼이 없음
        pass

    def sampling(self):
        df = pd.read_csv('../../../../static/save/dam/ml/stroke.csv')
        data = df.drop(['뇌졸중'],axis=1)
        target = df['뇌졸중']
        undersample = RandomUnderSampler(sampling_strategy=0.333, random_state=2)
        data_under, target_under = undersample.fit(data, target)
        X_train, X_test, y_train, y_test = train_test_split(data_under, target_under, test_size=0.5,
                            random_state=42, stratify=target_under)
        print('X_train shape:', X_train.shape)
        print('X_test shape:', X_test.shape)
        print('y_train shape:', y_train.shape)
        print('y_test shape:', y_test.shape)


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = StrokeService()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            stroke_menu[menu](t)
            '''
               try:
                   stroke_menu[menu](t)
               except KeyError:
                   print(" ### Error ### ")
               '''



