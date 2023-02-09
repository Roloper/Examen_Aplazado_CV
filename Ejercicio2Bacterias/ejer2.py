import cv2
import numpy as np
from stackImages import StackImagen

#Cargar la imagen
img = cv2.imread(r"imagenes2\bacteria.jpg")
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
        cv2.drawContours(img2,cnt,-1,(255,0,0),3)
        perimetro = cv2.arcLength(cnt,True)
        aprox = cv2.approxPolyDP(cnt,0.02*perimetro,True)
        objcorner=len(aprox)
        x,y,w,h = cv2.boundingRect(aprox)
        if objcorner >4:
            b = "Bacteria"
            cont=cont+1
        else:
            b = "?"
        cv2.rectangle(img2,(x,y),(x+w,y+h), (0,255,0),2)
        cv2.putText(img2, b,(x+(w//2)-18, y + (h//2)-18), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
    print("En esta imagen hay ",cont," BACTERIAS")
#Llamamos a la funcion
getContorno(borde)

#Mostrar las imágenes resultantes creando un objeto de la clase StackImagen
stack = StackImagen(0.4)
imagenes = [img,gris,gaus,borde,img2]


result = stack.stack_images(imagenes)
cv2.imshow("Resultado",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
