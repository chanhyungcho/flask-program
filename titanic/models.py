import pandas as pd

from util.dataset import Dataset


class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):   #데이터 수집
        pass

    def __str__(self):
        return f""

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:  #이 클래스 안에서 쓰일 인스턴스
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    def create_train(self):   #객체화
        pass

    def create_label(self):
        pass