from lena.models import LenaModel
from util.dataset import Dataset


class LenaController(object):

    dataset = Dataset()
    model = LenaModel()

    def __init__(self):
        pass

    def __str__(self):
        return f""

    def mining(self):
        pass

    def preprocess(self,fname) -> object:
        img = self.model.new_model(fname)
        return img

    def postprocess(self):
        pass

    def modeling(self,fname) -> object:
        img = self.preprocess(fname)
        return img

    def learning(self):
        pass

    def submit(self):
        pass

if __name__ == '__main__':
    pass