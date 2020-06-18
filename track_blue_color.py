import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Change colorspace
#pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2HSV)
while True:
	thr, frame = cap.read()
	pic = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 255, 255])

	mask = cv2.inRange(pic, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow("IMG2", res)

	if cv2.waitKey(25)&0xFF == ord('q'):
		break

cv2.destroyAllWindows()