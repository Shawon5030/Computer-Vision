import cv2
import numpy as np

img = cv2.imread('orginal.jpg')
img = cv2.resize(img,(600,400))
def nothing(x):
  pass

cv2.namedWindow('color',cv2.WINDOW_NORMAL)

cv2.createTrackbar('low_H','color',0,255,nothing)
cv2.createTrackbar('low_S','color',0,255,nothing)
cv2.createTrackbar('low_V','color',0,255,nothing)

cv2.createTrackbar('high_H','color',255,255,nothing)
cv2.createTrackbar('high_S','color',255,255,nothing)
cv2.createTrackbar('high_V','color',255,255,nothing)
 
while True:
 
 
 hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

 low_h = cv2.getTrackbarPos('low_H','color')
 low_s = cv2.getTrackbarPos('low_S','color')
 low_v = cv2.getTrackbarPos('low_V','color')

 high_h = cv2.getTrackbarPos('high_H','color')
 high_s = cv2.getTrackbarPos('high_S','color')
 high_v = cv2.getTrackbarPos('high_V','color')

 low = np.array([low_h,low_s,low_v])
 high = np.array([high_h,high_s,high_v])
 musk = cv2.inRange(hsv,low,high )

 result = cv2.bitwise_and(img,img,mask=musk)

 cv2.imshow('hsv',hsv)
 cv2.imwrite('Hsv.png',hsv)
 cv2.imshow('musk',musk)
 cv2.imwrite('musk.png',musk)
 cv2.imshow('result',result)
 cv2.imwrite('result.jpg',result)
 if cv2.waitKey(1) & 0xff == ord('q'):
  break 

cv2.destroyAllWindows()

