import cv2
import numpy as np

img_1 = cv2.imread("../samples/3D-Matplotlib.png")
img_2 = cv2.imread("../samples/Basic-Plot.png")

logo = cv2.imread("../samples/python.png")

add = img_1 + img_2

cv2.imshow("ADD", add)
cv2.waitKey(0)
cv2.destroyAllWindows()
