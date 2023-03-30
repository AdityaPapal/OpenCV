# Face Detection
import numpy as np
import cv2

face_classifiers = cv2.CascadeClassifier("Haarcascades\haarcascade_frontalface_default.xml")

image = cv2.imread('image_examples/obama.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # converting  RGB to GRAY

face= face_classifiers.detectMultiScale(gray,1.3,5)

if face is ():
    print("NO Face Found")


for (x,y,w,h) in face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,225),2)
    cv2.imshow("Face Detection",image)
    cv2.waitKey(0)

cv2.destroyAllWindows()