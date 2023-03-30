# Video captured

import  cv2
cap = cv2.VideoCapture("image_examples/demo.mp4")

while True:
    success,img = cap.read() #  type of success vairiable is bool
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

