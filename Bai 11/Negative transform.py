# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:18:05 2022

@author: ad
"""

import matplotlib.image as img
import numpy as np
from PIL import Image 


im = img.imread("Pictures/Fig0304(a)(breast_digital_Xray).tif")

im_negative = 255- im

#img.imsave("negative_img.tif",im_negative)

im_out= Image.fromarray(im_negative)
im_out.save("Pictures/nagative_imageXRay.tif")