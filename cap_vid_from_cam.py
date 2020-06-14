#Захватывает видео со встроенной камеры и выводит в небольшом 
#окне в ЧБ
import cv2
import numpy as np

#Инициализируем объект захвата изображения. вместо 0 можно
#указать название видео файла
cap = cv2.VideoCapture(0)

while (True):
	#cap.read выдаёт два значения: true при успешном захвате, и
	# кадр 
	ret, frame = cap.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', frame)
	#Здесь важно указать время задержки (число). Без него
	#захватывает только один кадр
	if cv2.waitKey(25) & 0xFF == ord('a'):
		break

cap.release()
