import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	'''
	#Scaling
	#rows, cols = grey.shape
	#res = cv2.resize(grey, None, fx=0.2, fy=0.2)
	'''
	'''#Moving pic in window
	#This row  represents the location for moving ([1, 0] on first and [0, 1] on second)
	#are constant, third num are ''coordinates''
	#M = np.float32([[1, 0, 200], [0, 1, 50]])
	#This row applies transformation on image
	#rows, cols = grey.shape
	#res = cv2.warpAffine(grey, M, (cols, rows))
	'''
	'''#Rotation (X - angle)
	#rows, cols = grey.shape
	#M = cv2.getRotationMatrix2D((cols/2, rows/2), X, 1)
	#res = cv2.warpAffine(grey, M, (cols, rows))
	'''
    '''#Affine transformation
	#pts1 = np.float32([[50,50],[200,50],[50,200]])
	#pts2 = np.float32([[10,100],[200,50],[100,250]])
	#rows, cols = grey.shape
	#M = cv2.getAffineTransform(pts1, pts2)
	#res = cv2.warpAffine(grey, M, (cols, rows))
	'''
	'''#Perspective Transformation
	rows, cols = grey.shape
	pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
	pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

	M = cv2.getPerspectiveTransform(pts1, pts2)
	res = cv2.warpPerspective(grey, M, (cols, rows))
	'''
	cv2.imshow("camera", res)
	if cv2.waitKey(25)&0xFF == ord('q'):
		break

cv2.destroyAllWindows()