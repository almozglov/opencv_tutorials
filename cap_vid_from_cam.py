import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', gray)
	print(cap.get(3))
	if cv2.waitKey(2) & 0xFF == ord('a'):
		break

cap.release()
