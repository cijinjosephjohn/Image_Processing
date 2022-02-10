
import cv2

image = cv2.imread("dices.png")


b, g, r = cv2.split(image)


cv2.imshow("Model Blue Image", b)

cv2.imshow("Model Green Image", g)


cv2.imshow("Model Red Image", r)


image_merge = cv2.merge([r, g, b])

cv2.imshow("RGB_Image", image_merge)


cv2.waitKey(0)
