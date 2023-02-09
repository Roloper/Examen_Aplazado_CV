import cv2
import numpy as np
from stackImages import StackImagen

# Carga la imagen
img = cv2.imread("imagenes1\pare_ejer1\pared.jpg")

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Convertir a HSL
#hsl_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# Aplicar un filtro Gaussiano para suavizar la imagen
gris = cv2.GaussianBlur(gris, (3,3), 0)

# Aplicar filtro Canny para detectar bordes
borde = cv2.Canny(gris, 10, 25)

# Encontrar los contornos en la imagen
contours, hierarchy = cv2.findContours(borde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una imagen de fondo blanco
contorno = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
contorno.fill(255)
# Dibujar los contornos en la imagen de fondo blanco
cv2.drawContours(contorno, contours, -1, (0, 0, 0), 2)
# Mostrar las imágenes resultantes creando un objeto de la clase StackImagen
stack = StackImagen(0.7)

imagenes = [img,gris
            ,borde,contorno]

result = stack.stack_images(imagenes)
cv2.imshow("Resultado",result)
cv2.waitKey(0)
cv2.destroyAllWindows()