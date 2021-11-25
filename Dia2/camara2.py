import cv2
import numpy as np

#Declarar parametros de color
colorin = np.array([20, 100, 100], np.uint8)
colorfn = np.array([35, 255, 255], np.uint8)

cam = cv2.VideoCapture(0)
while True:
    ban, frame = cam.read()
    if ban == True:
        #Invierte la imagen para no ser espejo
        frame = cv2.flip(frame,1)
        #COnvertir el fotograma a HSV
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Indicar el color a detectar en inicio y fin
        detector = cv2.inRange(frameHSV, colorin, colorfn)
        #Mostar el video del color detectado
        cv2.imshow('Sensor', detector)
        cv2.imshow('Tecnologia', frameHSV)
        cv2.imshow('WebCam On', frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
cam.release()
cv2.destroyAllWindows()
