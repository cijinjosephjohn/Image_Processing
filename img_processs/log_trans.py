import cv2
import numpy as np

img = cv2.imread('sunflower.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
c = 255/(np.log(1+ np.max(gray)))
log_trans = c * np.log(1+ gray)

log_trans = np.array(log_trans,dtype=np.uint8)

cv2.imshow("img",log_trans)
cv2.waitKey(0)
