import pandas as pd

from util.dataset import Dataset


class BicycleModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):

        '''return f'Train Type: {type()}'
        print(f'Train Type: {type(b)}')
        print(f'Train columns: {b.columns}')
        print(f'Train head: {b.head()}')
        print(f'Train null의 갯수: {b.isnull().sum()}')'''


    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    def create_train(self):
        pass

    def create_label(self):
        pass


