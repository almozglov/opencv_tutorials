import cv2
import numpy as np 
from matplotlib import pyplot as plt
img1 = cv2.imread('image.png')

#color of border
BLUE = [255,0,0]
while True:
	
	#cv2.imshow('MyPic', img)
	#access a single pixel value
	#print(img[50, 50])

	#modify single pixel value
	#img[i, i] = [0, 0, 0]

	#moving single part of image to another place
	#st_cell = img[10:90, 40:140]
	#img [10:90, 300:400] = st_cell

	#color spliting
	''' 
	b, g, r = cv2.split(img)
	cv2.imshow('B', b)
	cv2.imshow('G', g)
	cv2.imshow('R', r)
	cv2.imshow('Vollcolored', cv2.merge((b, g, r)))'''

	#making border
	#border = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 0, 0])

	#More border types
	'''
	replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
	reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
	reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
	wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
	constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
	'''
	#Code below to break window
	if cv2.waitKey(25)&0xFF == ord('q'):
		break