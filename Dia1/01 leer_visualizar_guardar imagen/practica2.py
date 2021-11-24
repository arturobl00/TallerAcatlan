import cv2
#Aplicación para activar la camara web

#Funcion para activar la camara el 0 es de indefinido
captura = cv2.VideoCapture(0)

#Funicon y variable para grabar el video
salida = cv2.VideoWriter('MiVideo.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

#para su uso empleamo un ciclo
while(captura.isOpened()):
    ret, video = captura.read()
    if ret == True:
        cv2.imshow('Mi WebCam', video)
        salida.write(video)

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break;

captura.release()
salida.release()
cv2.destroyAllWindows()