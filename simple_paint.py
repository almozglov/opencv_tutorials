import cv2 
import numpy as np 

drawing = False
mode = True
ix, iy = -1, -1

def nothing(x):
	pass

#creating black window
blank_img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Image')


#creating taskbars
cv2.createTrackbar('R', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('B', 'Image', 0, 255, nothing)
cv2.createTrackbar('Size', 'Image', 0, 100, nothing)

#Create ON/OFF switch
switch = '0: Circle \n1: Rectangle'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)


def draw_circle(event, x, y, flags, par):
	global ix, iy, drawing, mode
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			if mode:
				cv2.rectangle(blank_img, (ix, iy), (x, y), (r, g, b), -1)
			else:
				cv2.circle(blank_img, (ix, iy), size, (r, g, b), -1)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode:
			cv2.rectangle(blank_img, (ix, iy), (x, y), (r, g, b), -1)
		else:
			cv2.circle(blank_img, (ix, iy), size, (r, g, b), -1)

cv2.setMouseCallback('Image', draw_circle)
while True:
	

	cv2.imshow('Image', blank_img)
	key = cv2.waitKey(25)&0xFF
	if key == ord('q'):
		break

	#getting positions
	r = cv2.getTrackbarPos('R', 'Image')
	g = cv2.getTrackbarPos('G', 'Image')
	b = cv2.getTrackbarPos('B', 'Image')
	size = cv2.getTrackbarPos('Size', 'Image')
	sw = cv2.getTrackbarPos(switch, 'Image')

	if sw == 0:
		mode = False
	else:
		mode = True

cv2.destroyAllWindows()