# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 06:15:48 2022

@author: ad
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import scipy.misc
import numpy as np
#from scipy.misc.pilutil import Image
from PIL import Image
# opening the image and converting it to grayscale

#im = Image.open("../bugs.png").convert('L')
im= Image.open("Pictures/Fig0304(a)(breast_digital_Xray).tif").convert('L')

img_arr = np.array(im)

im2 = 255 - img_arr

new_img = Image.fromarray(img_arr)

new_img.save("Pictures/imageinverse_output.tif")
