import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)

#Configuracion de mediapipe
with mp_pose.Pose(
    static_image_mode = True,
    min_detection_confidence = 0.5) as pose:

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
        result = pose.process(frame_rgb)

        negro = np.zeros(frame.shape, np.uint8)

        if result.pose_landmarks is not None:
            mp_drawing.draw_landmarks(
                frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,0,0), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(255,255,255), thickness=6))
            
            mp_drawing.draw_landmarks(
                negro, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(255,255,255), thickness=6))
            
        #Mostrar video procesado
        cv2.imshow("Cam MediaPipe", frame)
        cv2.imshow("Cam Negra", negro)

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cam.realice()
cv2.destroyAllWindows()


