import cv2

from lena.views import LenaController
from util.common import Common

if __name__ == '__main__':
    api = LenaController()
    while True:
        menu = Common.menu(["종료","원본 보기"])
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("원본 보기")
            img = api.modeling('lena.jpg')
            print(f'cv2 버전 {cv2.__version__}')  # cv2 버전 4.6.0
            print(f' Shape is {img.shape}')
            cv2.imshow('Gray', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()