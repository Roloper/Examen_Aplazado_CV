import cv2
import numpy as np

# Leer la imagen
from stackImages import StackImagen

img = cv2.imread(r'imagenes/glaciar.jpg')
img2 = img.copy()
# Convertir la imagen a escala de grises
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro Gaussiano para suavizar la imagen
gaus = cv2.GaussianBlur(gris, (7,7), 0)

# Aplicar filtro Canny para detectar bordes
borde= cv2.Canny(gaus,50,50)

#Funcion para obtener area de las figuras que salen en la imagen
def getContorno(img):
    cont = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(img2,cnt,-1,(255,0,0),3)
        cont = cont +area
    print("El area total del glaciar es: ",cont)
#Llamamos a la funcion
getContorno(borde)

#Mostrar las imágenes resultantes creando un objeto de la clase StackImagen
stack = StackImagen(0.4)
imagenes = [img,gris,gaus,img2]


result = stack.stack_images(imagenes)
cv2.imshow("Resultado",result)
cv2.waitKey(0)
cv2.destroyAllWindows()