#Primer paso importar la libreria
import cv2

#Segundo declarar una variable y leer una imagen
img = cv2.imread('tec.png')

#Tercer paso Mostrar la imagen imshow
cv2.imshow('Imagen del Tec',img)

#Nota pausa de ventana y terminar programa
cv2.waitKey(0)
cv2.destroyAllWindows()

#Proceso para leer en escala de gris o inversa rgb a bgr
img = cv2.imread('tec.png',0)

#Tercer paso Mostrar la imagen imshow
cv2.imshow('Imagen del Tec bgr',img)

#Nota pausa de ventana y terminar programa
cv2.waitKey(0)

#Guardar una imagen
cv2.imwrite("tecgris.jpg",img)

cv2.destroyAllWindows()





