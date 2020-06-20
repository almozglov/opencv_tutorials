import cv2
import numpy as np

pic = cv2.imread('bp.jpg', 0)
cap = cv2.VideoCapture(0)

#image filtering (2D convolution)
#kernel = np.ones((5, 5), np.float32)/25
#res = cv2.filter2D(pic, -1, kernel)

#Bluring
#res = cv2.blur(pic, (5, 5))

#Gaussian Filtering
#res = cv2.GaussianBlur(pic, (5, 5), 0)

#Median filtering wow
#res = cv2.medianBlur(pic, 5)

#Bilateral filtering


while True:
	ret, frame = cap.read()
	res = cv2.GaussianBlur(frame, (10, 10), sigmaX = 10)
	cv2.imshow("BP", res)
	#cv2.imshow("BP", cv2.resize(erosion_maj, None, fx=0.5, fy=0.5))
	if cv2.waitKey(25)&0xFF == ord('q'):
		break

cv2.destroyAllWindows()