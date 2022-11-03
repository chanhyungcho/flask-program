import cv2
from matplotlib import pyplot as plt
from PIL import Image
from canny.services import ImageToNumberArray, GaussianBlur, Canny, ExecuteLambda
import cv2 as cv
import numpy as np

from util.dataset import Dataset

def image_read(fname) ->object: #전처리
    return (lambda x: cv2.imread('./data/' + x))(fname)

def menu_5(*params):
    ds = Dataset()
    girl = params[2]
    girl = cv.cvtColor(image_read(girl), cv.COLOR_BGR2RGB)

    print(params[0])
    img = cv.cvtColor(image_read(girl), cv.COLOR_BGR2RGB)
    print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
    plt.subplot(151), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.imshow((lambda x: Image.fromarray(x))(img))


    print(params[0])
    img = cv.cvtColor(image_read(girl), cv.COLOR_BGR2RGB)
    # 람다식 내부에서 GRAYSCALE 변환 공식 사용함
    img = (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(img)
    plt.subplot(152), plt.imshow(img, cmap='gray')
    plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
    plt.imshow((lambda x: Image.fromarray(x))(img))



    # img = GaussianBlur(img, 1, 1) cv.Canny() 를 사용하지 않는 경우 필요
    # img = Canny(img, 50, 150) cv.Canny() 를 사용하지 않는 경우 필요
    img = cv.cvtColor(image_read(girl), cv.COLOR_BGR2RGB)
    edges = cv.Canny(np.array(img), 100, 200)
    plt.subplot(153), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    print(params[0])
    img = cv.cvtColor(image_read(girl), cv.COLOR_BGR2RGB)
    edges = cv.Canny(img, 100, 200)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180., 10, minLineLength=50, maxLineGap=5)
    dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
    plt.subplot(154), plt.imshow(dst, cmap='gray')
    plt.title('Hough Image'), plt.xticks([]), plt.yticks([])

    print(params[0])
    # 모델 불러오기
    haar = cv.CascadeClassifier(f"{ds.context}{params[1]}")

    face = haar.detectMultiScale(girl, minSize=(150, 150))
    if len(face) == 0:
        print("얼굴인식 실패")
        quit()
    for (x, y, w, h) in face:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        red = (225, 0, 0)
        cv.rectangle(girl, (x, y), (x + w, y + h), red, thickness=20)

    cv.imwrite(f'{ds.context}girl-face.png', girl)
    plt.subplot(155), plt.imshow(girl, cmap='gray')
    plt.title('Haar Image'), plt.xticks([]), plt.yticks([])

    plt.show()
