import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')


img = cv2.imread('cat.png')
faces = face_cascade.detectMultiScale(img, 1.1, 6)

for (a,b,c,d) in faces:
    img = cv2.rectangle(img,(a,b),(a+c,b+d),(255,255,0),3)
    
    

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
