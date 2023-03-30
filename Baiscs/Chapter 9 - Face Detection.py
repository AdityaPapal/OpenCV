import cv2

path = "haarcascades/haarcascade_frontalface_default.xml"
facedetect = cv2.CascadeClassifier(path)
img = cv2.imread("image_examples/obama.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = facedetect.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

cv2.imshow("Result",img)
cv2.waitKey(0)