import cv2
import numpy as np

pic = cv2.imread('bp.jpg', 0)
ret, thr = cv2.threshold(pic, 127, 255, cv2.THRESH_BINARY_INV)

kernel_major = np.ones((5, 5), np.uint8)
kernel_minor = np.ones((3, 3), np.uint8)

#Thinner
#erosion_maj = cv2.erode(thr, kernel_major, iterations=1)
#cv2.dilate() have same args as cv2.erode()
#Negate noise ouside the fig
opening= cv2.morphologyEx(erosion_maj, cv2.MORPH_OPEN, kernel_major)

#Negate noise inside the fig
#closing= cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_major)
#closing_min= cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_minor)
#erosion_min = cv2.erode(erosion_maj, kernel_minor, iterations=1)
#laplacian = cv2.Laplacian(erosion, cv2.CV_64F)
while True:

	cv2.imshow("BP", cv2.resize(opening, None, fx=0.5, fy=0.5))
	#cv2.imshow("BP", cv2.resize(erosion_maj, None, fx=0.5, fy=0.5))
	if cv2.waitKey(25)&0xFF == ord('q'):
		break

cv2.destroyAllWindows()