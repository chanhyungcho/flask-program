import pandas as pd

from util.dataset import Dataset


# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#     'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
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
        pass

    def create_label(self):
        pass