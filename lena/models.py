from util.dataset import Dataset
import cv2

class LenaModel(object):
    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        return f""

    def preprocess(self):
        pass

    def new_model(self,fname):
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        img = cv2.imread(this.context + this.fname)
        return img