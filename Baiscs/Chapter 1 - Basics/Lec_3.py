# Face & eye Detection

import numpy as np
import cv2

face_classifiers = cv2.CascadeClassifier("Haarcascades\haarcascade_frontalface_default.xml")
eye_classifiers = cv2.CascadeClassifier("Haarcascades\haarcascade_eye.xml")

image = cv2.imread('image_examples/Trump.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face = face_classifiers.detectMultiScale(gray,1.3,5)

# if face is ( ):
#    print("Face is not Found")

for (x,y,w,h) in face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,225),2)
    cv2.imshow('Image',image)
    cv2.waitKey(0)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = image[y:y+h, x:x + w]
    eyes = eye_classifiers.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
        cv2.imshow('image',image)
        cv2.waitKey()

cv2.destroyAllWindows()