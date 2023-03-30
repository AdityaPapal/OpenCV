# Video captured
import  cv2
cap = cv2.VideoCapture(0)

path1 = "haarcascades/haarcascade_frontalface_default.xml"
path2 = "haarcascades/haarcascade_eyes.xml"

facedetect = cv2.CascadeClassifier(path1)
eyesdetect = cv2.CascadeClassifier("haarcascades/haarcascade_eyes.xml")



def detect(gray,frame):
    faces = facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eyesdetect.detectMultiScale(roi_gray,1.1,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    return frame

while True:
    _,frame= cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv2.imshow("Video",canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()