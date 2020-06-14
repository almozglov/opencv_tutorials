#unfinished VideoRecorder
#10.06.20

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#defining codec and creating VideoWriter obj
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		#frame = cv2.flip(frame, 0)
		output.write(frame)
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
output.release()
cv2.destroyAllWindows()