#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:59:28 2018

@author: jeffreybruggeman
"""

# Main
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, ndimage

# import image as greyscale
img=Image.open("Bacteria Dataset/PIL-338_3dayLBCR-4.jpg").convert('L')
# convert to array
a = np.array(img)
# save second copy of img array for trimming
arr_1=np.array(img)
# find dimensions of original for trimming
dim_orig = np.array(img).shape
# find mode of first x and y lines to establish background noise
mode_1 = stats.mode(a[0])
mode_2 = stats.mode(a[:,0])
# take min of those modes for ideal threshold
mode_min = min(mode_1[0], mode_2[0])
# Set all pixels 30 under threshold and 
a[a > mode_min-20] = 0
# check center of mass 1st time
CoM1=ndimage.measurements.center_of_mass(a)
# trim all 0 rows and columns
a=a[~np.all(a==0, axis=1)]
a=a[:,~np.all(a==0, axis=0)]
# check center of mass second time
CoM2=ndimage.measurements.center_of_mass(a)
# find dimensions of a for trimming
dim_a=a.shape
# show and annotate trimmed image
plt.imshow(a)
plt.annotate('Center of Mass', xy=CoM2, xycoords='data',
             xytext=(0.5, 0.5), arrowprops=dict(arrowstyle="->"))
plt.show()
# Find image shift based on center of mass
dimension1=CoM1[0]-CoM2[0]
dimension2=CoM1[1]-CoM2[1]
# trim original image
arr_2=arr_1[int(dimension1):int(dim_a[0]+dimension1), int(dimension2):int(dim_a[1]+dimension2)]
# show trimmed original
plt.imshow(arr_2)
plt.show()