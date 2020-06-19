import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Change colorspace
#pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2HSV)
while True:
	thr, frame = cap.read()
	
	lower_blue = np.array([100, 100, 100])
	upper_blue = np.array([135, 255, 255])
	lower_red = np.array([0, 100, 100])
	upper_red = np.array([10, 255, 255])


	mask_blue = cv2.inRange(pic, lower_blue, upper_blue)
	mask_red = cv2.inRange(pic, lower_red, upper_red)
	res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
	res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
	cv2.imshow("IMG2", cv2.add(res_blue, res_red))

	if cv2.waitKey(25)&0xFF == ord('q'):
		break

cv2.destroyAllWindows()