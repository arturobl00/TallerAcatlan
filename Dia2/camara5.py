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
        contorno,_ = cv2.findContours(detector, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contorno:
            area = cv2.contourArea(c)
            if area > 800:
                #Declaramos x para horizontal
                #y para vertical
                #w para el ancho
                #h para el alto y con boundingRect tomamos el valor
                x,y,w,h = cv2.boundingRect(c)
                #Dibujar un rectangulo y un texto
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(frame, 'Rojo', (x-10, y-10), 0, 1, (0,255,0), 2)
        
        cv2.imshow('WebCam Contornos', frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
cam.release()
cv2.destroyAllWindows()
