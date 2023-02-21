import cv2

trData  = cv2.CascadeClassifier('TRData.xml')

img = cv2.imread("FaceImages/2.jpg")

cv2.imshow('ck', img)
cv2.waitKey()

print("run")
