import cv2
import numpy as np
from stackImages import StackImagen

def getContorno(img):




#Cargar la imagen
img = cv2.imread(r"imagenes2\bacterias.jpg")

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro Gaussiano para suavizar la imagen
gaus = cv2.GaussianBlur(gris, (7,7), 0)

# Aplicar filtro Canny para detectar bordes
borde= cv2.Canny(gaus,50,50)


stack = StackImagen(0.8)

imagenes = [img,gris,gaus,borde,]

result = stack.stack_images(imagenes)
cv2.imshow("Resultado",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
