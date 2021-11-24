import cv2

img = cv2.imread('tec.png')

cv2.imshow("Ventana imagen", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

