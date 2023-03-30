import cv2
import numpy as np


img = cv2.imread("image_examples/obama.jpg")
kernel = np.ones((5,5),np.uint8)

# RGB to Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 7by7 is kernel size n 0 is sigma
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

# Canny use for edges director and 100 by 100 is Threshold value
imgCanny = cv2.Canny(img,100,100)

# Dilation is use of more accuracy in ede detection
# in kernel we have to add sizeof and valueof
# in this kernel we also need to define size of matrix
imgDialition = cv2.dilate(imgCanny,kernel,iterations=1)

# opposite of dialation is erossion
imgeroded = cv2.erode(imgDialition,kernel,iterations=1)


cv2.imshow('imgeroded Image',imgeroded)
cv2.imshow("Dialition Image",imgDialition)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow('Elephant Image',imgGray)


cv2.waitKey(0)
cv2.destroyAllWindows()