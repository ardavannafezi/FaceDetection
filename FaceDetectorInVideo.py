import cv2

trData  = cv2.CascadeClassifier('TRData.xml')

webcam = cv2.VideoCapture(0)
while True: 
    seccessFrame ,  frame = webcam.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faceCordinate = trData.detectMultiScale(grayscale)
    
    for(x,y,w,h) in faceCordinate:
        cv2.rectangle(frame, (x, y), (x+w , y+h), (0,255,0), 5)

    
    cv2.imshow('ck', frame)
    key = cv2.waitKey(1)
    
    if key == 81 or key == 113:
        break
    
webcam.release()