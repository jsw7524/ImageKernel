import numpy as np
import cv2

#source=np.arange(100).reshape(10,10)
source = cv2.imread('Waku.jpg')
source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
target=np.zeros(source.shape,dtype=np.uint8)
kernel=np.array([[-2,-1,0],
                 [-1,1,1],
                 [0,1,2]])
# kernel=np.array([[-1,0,1],
#                  [-2,0,2],
#                  [-1,0,1]])
for y in range(1,source.shape[0]-1):
    for x in range(1,source.shape[1]-1):
            tmp=(source[y-1:y+2,x-1:x+2]*kernel).sum()
            if tmp > 255:
                target[y,x]=255
            elif tmp < 0:
                target[y,x]=0
            else:
                target[y,x]=tmp
                
#print(target)
cv2.imshow('source', source)        
cv2.imshow('target', target)
cv2.waitKey(0)