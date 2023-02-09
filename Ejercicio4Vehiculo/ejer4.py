import cv2 # opencv library
import numpy as np



#VIdeo importado
vid = cv2.VideoCapture(r'recursos\video.mp4')

#tamaño minimo del objeto
min_width_react=80
min_hight_react=80

count_line_postion = 550 #Para asignar la posicion de la linea


#Inicializando el Subestructurado, trata de quitar el fondo y enfocar el objeto en movimiento
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

#Calcular el centro del objeto
def center_handle(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx = x+x1
    cy = y + y1
    return cx,cy

detect = []
offset = 6 #error permitido entre píxeles
cont = 0

while True:
    #La función ret, frame1 = vid.read() devuelve dos valores:
    # ret es un valor booleano que indica si el fotograma se ha leído correctamente,
    # y frame1 es una matriz NumPy que representa el fotograma.
    ret, frame1 = vid.read()

    #Ponindo el frame en escala de grises
    gris = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

    #Suavisando la imagen con el filtro Gausianico
    gaus = cv2.GaussianBlur(gris,(3,3),5)

    #Aplicamos a cada frame el Substructurado
    img_sub = algo.apply(gaus)

    #Dilatamos los elementos de la imagen
    dilat = cv2.dilate(img_sub,np.ones((5,5)))

    #
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

    #Se cierra las pequeñas brechas de la imagen binaria
    dilatada = cv2.morphologyEx(dilat,cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)

    #
    counterShape,h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1,(25,count_line_postion),(1200, count_line_postion),(255,127,0),3)


    for (i,c) in enumerate(counterShape):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_counter = (w>= min_width_react) and (h>= min_hight_react)
        if not validate_counter:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
        center = center_handle(x,y,w,h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0,255,0), -1)

        for(x,y) in detect:
            if y < (count_line_postion+offset) and y > (count_line_postion-offset):
                cont= cont+1
            cv2.line(frame1,(25,count_line_postion),(1200, count_line_postion),(0,127,255),3)
            detect.remove((x,y))
            print("vehiculo contado: ", cont)

    cv2.putText(frame1,"Vehiculo contado: "+str(cont),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),5)


    cv2.imshow('Video',frame1) #muestar el fotograma

    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllwindows()
vid.release()