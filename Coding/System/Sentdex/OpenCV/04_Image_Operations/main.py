import numpy as np
import cv2

img = cv2.imread("../samples/port.JPG", cv2.IMREAD_COLOR)

# From img(y=500, x=55), assign single pixel to px
px = img[500,55]

# Modify the pixel
img[460,60] = [255,0,255]
# img[y(row), x(column)]
# `row` the order is from the top to the bottom.
# `column` the order is from the left to the right.

# Assign a region to rgn
rgn = img[100:150, 100:150]
# Change a region's colour.
img[100:150, 100:150] = [255,255,255]

# Assign a region to another region
sun = img[470:530, 440:520]
img[0:60, 0:80] = sun

cv2.imshow("IMAGE", img)
cv2.moveWindow("IMAGE", 30, 30)
cv2.waitKey(0)
cv2.destroyAllWindows()
