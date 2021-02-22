import cv2
import numpy as np
from matplotlib import pyplot as plt
imgPath = './Resources/t1.jpg'
heightImg = 450
widthImg = 720

img1=cv2.imread(imgPath)
img1=cv2.resize(img1,(widthImg,heightImg))
img=cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(widthImg,heightImg))
imgb=cv2.imread(imgPath,cv2.COLOR_BGR2RGB)
imgb=cv2.resize(imgb,(widthImg,heightImg))


lap=cv2.Laplacian(img,cv2.CV_64F,ksize=9)
lap=np.uint8(np.absolute(lap))
cv2.imshow('lap',lap)



kernal=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(imgb,-1,kernal)
blur=cv2.blur(imgb,(5,5))
gb=cv2.GaussianBlur(imgb,(5,5),0)
bf=cv2.bilateralFilter(imgb,9,75,75)
# cv2.imshow('b1',dst)
# cv2.imshow('b2',blur)
# cv2.imshow('gb',gb)
# cv2.imshow('bf',bf)

# def demo(x):
#     print(x)
#
# cv2.namedWindow('track')
# cv2.createTrackbar('val','track',0,255,demo)
#
# while True:
#     val = cv2.getTrackbarPos('val', 'track')
#     _,mask=cv2.threshold(lap,val,255,cv2.THRESH_BINARY_INV)
#     cv2.imshow('track',mask)
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
#



cv2.imshow('img',img1)
cv2.waitKey(0)