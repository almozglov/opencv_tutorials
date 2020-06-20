import cv2
import numpy as np

pic = cv2.imread('bp.jpg', 0)
ret, thr = cv2.threshold(pic, 127, 255, cv2.THRESH_BINARY)
laplacian = cv2.Laplacian(thr, cv2.CV_64F)
#laplacian_orig = cv2.Laplacian(pic, cv2.CV_64F)
#sobel сильно теряет в качестве, увы
sobelx = cv2.Sobel(laplacian, cv2.CV_64F, 1, 0, ksize=5)

while True:


	cv2.imshow("BP", cv2.resize(sobelx, None, fx=0.5, fy=0.5 ))
	if cv2.waitKey(25)&0xFF == ord('q'):
		break

cv2.destroyAllWindows()