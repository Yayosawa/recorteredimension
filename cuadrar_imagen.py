# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:22:31 2021

@author: Yayo
"""

import cv2

def cuadrarImagen(rutaImagen):

    img = cv2.imread(rutaImagen)
    alto, ancho = img.shape[0:2]

    primeraFila = 0
    primeraColumna = 0
    ultimaFila = alto
    ultimaColumna = ancho

    if alto > ancho:
        primeraFila = int((alto - ancho) / 2)
        ultimaFila -= int((alto - ancho) / 2)
    elif alto < ancho:
        primeraColumna = int((ancho - alto) / 2) 
        ultimaColumna -= int((ancho - alto) / 2) 
    else:
        pass
    imgCortada = img[primeraFila:ultimaFila, primeraColumna:ultimaColumna]
    cv2.imwrite(rutaImagen,imgCortada)
