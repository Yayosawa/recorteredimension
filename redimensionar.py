# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:21:32 2021

@author: Yayo
"""

from PIL import Image
import os
def redimensionarImagenes(directorioImagenes):
    arreglo_nombres_imagenes=os.listdir(directorioImagenes)
    for imagen in arreglo_nombres_imagenes:
        img = Image.open(directorioImagenes+imagen)
        img = img.resize((300,300))
        img.save(directorioImagenes+imagen)