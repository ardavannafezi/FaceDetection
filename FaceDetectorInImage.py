import cv2

trData  = cv2.CascadeClassifier('TRData.xml')

img = cv2.imread("FaceImages/2.jpg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceCordinate = trData.detectMultiScale(grayscale)


for(x,y,w,h) in faceCordinate:
    cv2.rectangle(img, (x, y), (x+w , y+h), (0,255,0), 5)


cv2.imshow('ck', img)

cv2.waitKey()
print("run")
