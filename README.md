# 20190717

PCのカメラの映像からデータを取り込み,画像の輝度値の平均値をグラフとしてプロットするプログラム.
ソースコードを以下に示す.

```
%matplotlib nbagg
# OpenCV のインポート
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt


# VideoCaptureのインスタンスを作成する。
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
```

frameに代入された各画素の輝度値の平均をframe.mean()で求め,
for文中でx,yにグラフのプロットに必要な値をそれぞれ追加し,ループが終了したらグラフを出力する.

![実行結果](cameragraph.gif) 

python3.7, opencv4.0.1を使用し,Jupiter notebookで作成・実行した.

参考URL：
Python+OpenCVでWebカメラの画像を取り込んで処理して表示する話: https://ensekitt.hatenablog.com/entry/2017/12/19/200000
Python: matplotlib で動的にグラフを生成する: https://blog.amedama.jp/entry/2018/07/13/001155

![cameragraph](https://user-images.githubusercontent.com/52983217/61575587-48bdd800-ab08-11e9-92e1-d17f5221242a.gif)
