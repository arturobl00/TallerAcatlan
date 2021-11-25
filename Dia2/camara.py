#paso1 importar las librerias
import cv2
import numpy as np

#paso2 declarar variable camara
cam = cv2.VideoCapture(0)

#paso3 invocar un ciclo para el control de la camara
while True:
    #paso4 declarar 2 variables la 1ra para el estado y la 2da para captura fotogramas
    ban, frame = cam.read()

    #paso5 pregunta si ban esta en true para mostrar fotogramas
    if ban == True:
        cv2.imshow('WebCam On', frame)

        #paso6 condicion de termino o cierre
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cam.release()
cv2.destroyAllWindows()
