import cv2
import numpy as np

#draw simple circles 
'''def draw_circle(event, x, y, flags, par):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img, (x, y), 20, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Draw Area')
cv2.setMouseCallback('Draw Area', draw_circle)

while True:
	cv2.imshow('Draw Area', img)
	if cv2.waitKey(20) & 0xFF==ord('a'):
		break
cv2.destroyAllWindows()
'''
#advanced
# Press M to change drawing mode (from squares to circles)
#press q to quit
drawing = False
mode = True
ix, iy = -1, -1

def draw_circle(event, x, y, flags, par):
	global ix, iy, drawing, mode
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			if mode:
				cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
			else:
				cv2.circle(img, (ix, iy), 5, (0, 0, 0), -1)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode:
			cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
		else:
			cv2.circle(img, (ix, iy), 5, (0, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Draw Area')
cv2.setMouseCallback('Draw Area', draw_circle)

while True:
	cv2.imshow('Draw Area', img)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('m'):
		mode = not mode
	elif key == ord('q'):
		break

cv2.destroyAllWindows()