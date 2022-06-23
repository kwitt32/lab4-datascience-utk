#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 07:08:58 2022

@author: n44
"""

import rasterio
from matplotlib import pyplot

#Ignore the "Not georeferenced warning"
#Make sure the path is set up properly so that the files can be accessed. I left my path in as an example.

dataset = rasterio.open(r'C:\Users\uwitk001\lab 4\knoxville.JPG')


#Reading Raster Data

band1 = dataset.read(1)
band2 = dataset.read(2)
band3 = dataset.read(3)

#Plot each one at a time or you will not see them all. 
pyplot.imshow(band1)

pyplot.imshow(band2)

pyplot.imshow(band3)

#What do you notice with each of the above bands? What is happening as the different ones are plotted? 
#Answer this on your answer sheet. 


#While the above are not necessary errors 
#what would you want to keep in mind when using these different bands in an analysis?
#Answer this on your answer sheet. 

band1
