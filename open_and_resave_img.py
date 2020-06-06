import cv2

img = cv2.imread('avatar.jpg', 1)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite('pic2.png', img)