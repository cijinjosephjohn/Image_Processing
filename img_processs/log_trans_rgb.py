

import cv2
import numpy as np

image = cv2.imread("dices.png")
b, g, r = cv2.split(image)
cv2.imshow("Model Blue Image", b)
c_b = 255/(np.log(1+ np.max(b)))
log_trans_b = c_b * np.log(1+ b)

log_trans_b = np.array(log_trans_b,dtype=np.uint8)

cv2.imshow("Model Green Image", g)
c_g = 255/(np.log(1+ np.max(g)))
log_trans_g = c_g * np.log(1+ g)

log_trans_g = np.array(log_trans_g,dtype=np.uint8)

cv2.imshow("Model Red Image", r)
c_r = 255/(np.log(1+ np.max(r)))
log_trans_r = c_r * np.log(1+ r)

log_trans_r = np.array(log_trans_r,dtype=np.uint8)

image_merge = cv2.merge([log_trans_r, log_trans_g, log_trans_b])
cv2.imshow("RGB_Image", image_merge)
cv2.waitKey(0)
