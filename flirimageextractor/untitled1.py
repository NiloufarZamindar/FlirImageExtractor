#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:21:23 2023

@author: ai
"""
import cv2
import numpy as np
import glob

from flirimageextractor import thermal_base


flir = thermal_base.ThermalSeqVideo('./Seconda_piastra_parte1_MIG.SEQ')
bb =flir.split_thermal('./Seconda_piastra_parte1_MIG.SEQ')



img_array = []

for filename in glob.glob('Seconda_piastra_parte1_MIG/*.jpg'):
    img = cv2.imread(filename)
    #height, width, layers = img.shape
    #size = (width,height)
    img_array.append(img)
width = 366
height = 240
size =(width,height)
video_length = 100

out = cv2.VideoWriter('flir.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(video_length):
    out.write(img_array[i])
out.release()