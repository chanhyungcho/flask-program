from titanic.models import TitanicModel
from util.dataset import Dataset


class TitanicController(object):

    model = TitanicModel()
    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = TitanicModel()

    def mining(self): # 원래 있어야
        pass

    def preprocess(self,train,test) -> object: #전처리
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.td = this.test['PassengerId']
        #columns 편집과정'
        #this = model.pclass_ordinal(this) 데이터 자체가 이미 ordinal이라 손댈 필요가 없음.
        this = model.sex_nominal(this) #this는 자료구조라서 이렇게 가능. 변수였으면 이렇게 불가. 사람 != 홍길동, 홍길동 == 사람
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_nominal(this)
        this = model.title_nominal(this)
        this = model.drop_features(this,
                                   'PassengerId','Name', 'Sex', 'Age',
                                   'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin')
        return this


    def postprcess(self): #원래 필요
        pass

    def modeling(self,train,test) -> object: #모델생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this

    def learning(self) -> object: #기계학습
        pass

    def submit(self): #배포
        pass

if __name__ == "__main__":
    t = TitanicController()
    this = Dataset()
    this = t.modeling('train.csv','test.csv')
    print(this.train.columns)
    print(this.train.head())

