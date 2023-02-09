import cv2
import numpy as np

#Cargar la imagen
img = cv2.imread(r"imagenes2\bacterias.jpg")

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()