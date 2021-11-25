import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)

#Configuracion de mediapipe
with mp_hands.Hands(
    static_image_mode = True,
    max_num_hands = 2,
    min_detection_confidence = 0.5) as hands:

    #leer video
    while True:
        ban, frame = cam.read()
        if ban == False:
            break

        #var para el alto y ancho de la cara
        height, width, _ = frame.shape

        #Invertir el video
        frame = cv2.flip(frame,1)

        #Cambiar frame a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        #TOmar datos
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks is not None:

            index = [4,8,12,16,20]
            #index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                #Ciclo para mostrar los puntos de la mano
                for (i, points) in enumerate(hand_landmarks.landmark):
                    if i in index:
                        x = int(points.x * width)
                        y = int(points.y * height)
                        cv2.circle(frame, (x,y), 14, (255,0,0), -1)
                        cv2.circle(frame, (x,y), 10, (0,0,255), -1)

        #Mostrar video procesado
        cv2.imshow("Cam MediaPipe", frame)

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cam.realice()
cv2.destroyAllWindows()


