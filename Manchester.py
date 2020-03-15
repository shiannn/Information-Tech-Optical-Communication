import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

from decode import decode

#cap = cv2.VideoCapture('camcom_testdata.mp4')
if(len(sys.argv) != 2):
    print('wrong format!')
    sys.exit(0)
cap = cv2.VideoCapture(sys.argv[1])
if(cap.isOpened()==False):
    print('Video not exist!')
    sys.exit(0)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

Black = -1
White = 1
count = 0
Prev = 0

oneDsignal = []
while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == 0):
        break
    count += 1
    #print(frame.shape)
    TotalIntensity = np.sum(frame)
    #print(TotalIntensity)
    frame = cv2.resize(frame,(100,100))
    cv2.imshow('frame',frame)

    if(TotalIntensity > 100000000):
        print('White')
        oneDsignal.append(1)
        """
        if(count % 2 ==0):
            if(Prev == Black):
                print('White to Black')
        Prev = White
        """
    else:
        print('Black')
        oneDsignal.append(0)
        """
        if(count % 2 ==0):
            if(Prev == White):
                print('Black to White')
        Prev = Black
        """

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(oneDsignal)
xlen = len(oneDsignal)
Xtemp = list(range(0,xlen))
X = [a/30 for a in Xtemp]

plt.step(X,oneDsignal)
plt.show()

mydecode = decode(oneDsignal)
result = 0
for i in range(12):
    if(mydecode[i]==1):
        result += 2**(11-i)
print(result)