import cv2
import numpy as np 
pic1 = cv2.imread('image2.png')
logo = cv2.imread('opencv.png')
rows, cols, channels = logo.shape
roi = pic1[0:rows, 0:cols]
#print(pic1.shape)
#print(logo.shape)
graylogo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(graylogo, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

pic1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)
	#blending images (2nd and 4th params is transparency. Last one is lambda (total whiteness))
	#fin = cv2.addWeighted(pic1, 0.5, pic2, 0.5, 0)
fin = cv2.add(pic1_bg, logo_fg)
pic1[0:rows, 0:cols] = fin

cv2.imshow("IMG2", pic1)
cv2.waitKey(0)
cv2.destroyAllWindows()