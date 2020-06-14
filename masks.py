import cv2
import numpy as np 
pic1 = cv2.imread('pic1.jpg')
pic2 = cv2.imread('pic2.jpg')
logo = cv2.imread('opencv.png')

row, col, channel = logo.shape
roi = pic1[0:row, 0:col]

logogray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logogray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

logo_bg = cv2.bitwise_and(logo, logo, mask=mask)
fin = cv2.add(pic1, logo_bg)

while True:
	#blending images (2nd and 4th params is transparency. Last one is lambda (total whiteness))
	#fin = cv2.addWeighted(pic1, 0.5, pic2, 0.5, 0)


	cv2.imshow("IMG", fin)
	
	if cv2.waitKey(25)&0xFF == ord('q'):
		break