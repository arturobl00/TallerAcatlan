#Importar librerias
import cv2
import mediapipe as mp

#Crear los metodos de mediapipe
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)

#Configuracion de mediapipe
with mp_face_mesh.FaceMesh(
    static_image_mode = True,
    max_num_faces = 2,
    min_detection_confidence = 0.5) as face_mesh:

    #leer video
    while True:
        ban, frame = cam.read()
        if ban == False:
            break

        #var para el alto y ancho de la cara
        height, width, _ = frame.shape
        #Cambiar frame a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #TOmar datos
        result = face_mesh.process(frame_rgb)

        if result.multi_face_landmarks is not None:
            for face_landmark in result.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    frame, face_landmark, mp_face_mesh.FACE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,255), thickness = 1, circle_radius = 1),
                    mp_drawing.DrawingSpec(color=(255,0,255), thickness = 1)
                )
        
        #Mostrar video procesado
        cv2.imshow("Cam MediaPipe", frame)

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cam.realice()
cv2.destroyAllWindows()


