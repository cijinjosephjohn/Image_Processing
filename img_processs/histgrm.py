import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sunflower.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',gray)

histgrm = cv2.calcHist([gray],[0],None,[256],[0,256])

plt.plot(histgrm)
plt.show()