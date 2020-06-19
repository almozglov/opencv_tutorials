import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Change colorspace
#pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2HSV)
#pic= cv2.imread('pic1.jpg', 0)
while True:
	thr, frame = cap.read()
	pic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	ret, thresh1 = cv2.threshold(pic, 127, 255, cv2.THRESH_BINARY)
	thresh2 = cv2.adaptiveThreshold(pic,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY ,11,2)
	thresh3 = cv2.adaptiveThreshold(pic, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)
	ret2, thresh4 = cv2.threshold(pic, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	#Otsu`s thresholding after Gaussian filtering
	blur = cv2.GaussianBlur(pic, (5, 5), 0)
	ret3, thr5 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	for i in range(5):
		cv2.imshow('image', thresh1)
		cv2.imshow('MEANc', thresh2)
		cv2.imshow('Gaussian', thresh3)
		cv2.imshow('Otsu', thresh4)
		cv2.imshow('Otsu+Gaussian', thr5)
	if cv2.waitKey(25)&0xFF == ord('q'):
		break

cv2.destroyAllWindows()