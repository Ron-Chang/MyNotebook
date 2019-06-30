import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image and convert grayscale
img = cv2.imread("../samples/port.JPG", cv2.IMREAD_GRAYSCALE)
# imread stand for IMage READ
# in the case of CV, the full colour image is BGR(A) (Blue, Green, Red, Alpha)

# cv2.IMREAD_GRAYSCALE = 0
# cv2.IMREAD_COLOR = 1
# cv2.IMREAD_UNCHANGED = -1

# Method #1 - Display by standard method
cv2.imshow("image", img)
# imshow = IMage SHOW
# cv2.imshow(window_name, image)

cv2.waitKey(0)
# Displayed it until manually close
# The unit is millisecond

# cv2.destroyAllWindows()


# # Method #2 - Display by matplotlib
# plt.imshow(img, cmap="gray", interpolation="bicubic")
# # plt is RGB order to display the image which is opposite way as cv2
# x = [0,700] # [x1, x2, x3]
# y = [0,500] # [y1, y2, y3]
# plt.plot(x, y, "r--", linewidth=5)
# plt.show()

# To save the current image
cv2.imwrite("new.png", img)
