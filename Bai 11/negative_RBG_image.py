# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:48:15 2022

@author: ad
"""


import matplotlib.image as img
import numpy as np
from PIL import Image

from matplotlib import pyplot as plt


im = img.imread("../flowers.jpg")

plt.subplot(121)
plt.imshow(im)



#im[im<0.5] = 0
#im[im>0.5] = 1
#
#
im = im.mean(axis=2)
im_out = 255-im
plt.subplot(122)
plt.imshow(im_out,cmap='gray')


