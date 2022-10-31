from lenna.models import LennaModel
from util.dataset import Dataset


class LennaController(object):

    dataset = Dataset()
    model = LennaModel()

    def __init__(self):
        pass

    def __str__(self):
        return f""

    def preprocess(self,fname) -> object:
        img = self.model.new_model(fname)
        return img

    def modeling(self,fname) -> object:
        img = self.preprocess(fname)
        return img

    def learning(self):
        pass

    def submit(self):
        pass

if __name__ == '__main__':
    pass