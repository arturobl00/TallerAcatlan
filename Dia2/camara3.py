import cv2
import numpy as np

colorin = np.array([0, 100, 100], np.uint8)
colorfn = np.array([10, 255, 255], np.uint8)

cam = cv2.VideoCapture(0)
while True:
    ban, frame = cam.read()
    if ban == True:
        frame = cv2.flip(frame,1)
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        detector = cv2.inRange(frameHSV, colorin, colorfn)
        maskRed = cv2.bitwise_and(frame, frame, mask = detector)
        #Mostar el video del color detectado
        cv2.imshow('Cam Bitwise', maskRed)
        cv2.imshow('WebCam On', frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
cam.release()
cv2.destroyAllWindows()
