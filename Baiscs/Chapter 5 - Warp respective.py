# Warp respective
import cv2
import numpy as np

img = cv2.imread("image_examples/cards.jpg")
print(img.shape)

width , height = 250,350 # ,
pt1= np.float32([[277,115],[453,129],[263,354],[458,375]])

pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
pt3= np.float32([[111,219],[287,188],[154,482],[352,440]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Image",imgoutput)
cv2.waitKey(0)
