import cv2 
import numpy as np 

def nothing(x):
	pass

#creating black window
blank_img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Image')

#creating taskbars
cv2.createTrackbar('R', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('B', 'Image', 0, 255, nothing)

#Create ON/OFF switch
switch = '0: OFF \n1: ON'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

while True:
	cv2.imshow('Image', blank_img)
	key = cv2.waitKey(25)&0xFF
	if key == ord('q'):
		break

	#getting positions
	r = cv2.getTrackbarPos('R', 'Image')
	g = cv2.getTrackbarPos('G', 'Image')
	b = cv2.getTrackbarPos('B', 'Image')
	sw = cv2.getTrackbarPos(switch, 'Image')

	if sw == 0:
		blank_img[:]
	else:
		blank_img[:] = [r, g, b]

cv2.destroyAllWindows()