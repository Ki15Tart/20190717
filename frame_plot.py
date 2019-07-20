%matplotlib nbagg
# OpenCV のインポート
import cv2

import itertools
import math

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
cap = cv2.VideoCapture(0)

y = []
x = []

for i in range(500):
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()
    cv2.imshow('Frame', frame)
    
    y.append(frame.mean())
    x.append(i)
    
    k = cv2.waitKey(1)
    if k == 27:
        break


plt.plot(x, y)
# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()
