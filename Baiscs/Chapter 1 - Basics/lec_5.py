# Video captured

import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) # 3 is Id for height
cap.set(4,480) # 4 is id for width
cap.set(10,100) # 3 is Id for height


while True:
    success, img = cap.read()  # type of success vairiable is bool
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

