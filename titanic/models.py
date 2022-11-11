import numpy as np
import pandas as pd
from util.dataset import Dataset
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#     'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#시각화를 통해 얻은 상관관계 변수(variable = feature = column)는
#Pclass
#Sex
#Age
#Fare
#Embarked
# ===null 값===
# Age            177
# Cabin          687
# Embarked         2

class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):   #데이터 수집
        pass


    def __str__(self):
        b = self.new_model(self.dataset.fname) #fname이라고만 해줬는데 컴터가 게터인지 세터인지 어케 이해? 똑같은데
        return f"Train Type: {type(b)}\n" \
               f'Train columns: {b.columns}\n' \
               f'Train head: {b.head()}\n' \
               f'Train null의 갯수: {b.isnull().sum()}'
        #print(f'Train Type: {type(b)}')
        #print(f'Train columns: {b.columns}')
        #print(f'Train head: {b.head()}')
        #print(f'Train null의 갯수: {b.isnull().sum()}')

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:  #이 클래스 안에서 쓰일 인스턴스
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname) #this context 쌀 pd.찧고 return 떡.


    @staticmethod
    def create_train(this) ->object:   #객체화
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this) ->object:
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object: # * > [ ] 자료구조의 의미
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this

    #원래 pclass가 들어가지만 숫자로 되어 있어서 컴퓨터에서 알아서 가능
    @staticmethod
    def sex_nominal(this)-> object: #female > 1, male > 0
         for i in [this.train,this.test]:
             i["Gender"] = i["Sex"].map({"male" : 0, "female" : 1})#gender는 0,1 sex는 male female
         return this

    @staticmethod
    def age_ordinal(this)-> object: #연령대 10대,20대,30대
        for i in [this.train,this.test]:
            i["Age"] = i["Age"].fillna(-0.5)
        bins = [-1,0,5,12,18,24,35,68,np.inf] #bins는 자료에서 하나씩 빼는것, 구간을 나눈것. -1~0:Unknown, 0~5:Baby
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior'] #영어로 먼저 설정
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, #매핑
                             'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in[this.train,this.test]:
            i["AgeGroup"] = pd.cut(i['Age'], bins=bins, labels=labels)
            i["AgeGroup"] = i["AgeGroup"].map(age_mapping)
        return this

    @staticmethod
    def fare_ordinal(this)-> object: #비싼 것, 보통, 저렴한것 #4등분 pd.qcut()사용
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels={1,2,3,4})
        return this

    @staticmethod
    def embarked_nominal(this)-> object: #승선항구 S,C,Q
        this.train = this.train.fillna({'Embarked': 'S'})  # 임시값을 집어넣어라 / fillna /na = not a number
        this.test = this.test.fillna({'Embarked': 'S'})  # 임시값을 집어넣어라 / fillna /na = not a number
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C": 2, "Q": 3}) # = 어사인먼트 asignment / map 매핑
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-Za-z]+)\.', expand=False) #i가 리스트였으면 i['']
        for i in combine:
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            i['Title'] = i['Title'].replace('Mlle', 'Mr')
            i['Title'] = i['Title'].replace('Ms', 'Miss')
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map({
                'Mr': 1,
                'Miss': 2,
                'Mrs': 3,
                'Master': 4,
                'Royal': 5,
                'Rare': 6
            })

        return this

    @staticmethod
    def create_k_fold() -> object: #생성자
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this,algo):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv =TitanicModel.create_k_fold(),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score)*100,2)

if __name__ == "__main__":  #스테틱 같은 공간 # main이라 self가 아님
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.title_nominal(this) #
    print(this.train.columns)
    print(this.train.head()) #위에서 부터 몇 개 볼지 tail()은 아래서 몇개볼지