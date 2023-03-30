# Shapes and Texts
import cv2
import numpy as np

img1 = np.zeros((512,512,3),np.uint8)
img2 = np.ones((512,512))
#print(img1)
#img1[100:400]= 225,0,0

cv2.line(img1,(0,0),(300,300),(0,255,0),3)
#            starting    ending

cv2.rectangle(img1,(0,0),(250,300),(0,0,255),cv2.FILLED) # x,y,h,w
cv2.circle(img1,(400,50),30,(255,255,0),5) # center ,radius,color


cv2.putText(img1,"OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)
# img-text-origin-font-font Scale-color- thickness


cv2.imshow("Black Img",img1)
#cv2.imshow("White Img",img2)

cv2.waitKey(0)
