import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)

#  To create a black image through numpy
img = np.zeros([512,512,3], np.uint8)

# Add a line
img = cv2.line(img, (0,0), (255,255), (181,74,84), 10)
# cv2.line(img, pt1, pt2, color(BGR), thickness, lineType, shift)
# Be aware of the color parameter the colour order is Blue Green Red

# Add an arrow
img = cv2.arrowedLine(img, (0,255), (255,255), (148,36,249), 10)

# Add a rectangle
img = cv2.rectangle(img, (300,0), (510,128), (0,200,200), -1)
# cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# pt1 is top-left and pt2 is bottom-right
# if thickness < 0, it will show a filled rectangle.

img = cv2.circle(img, (255,255), 50, (0,0,180), 7)
# img = cv2.circle(img, center, radius, color, thickness, lineType, shift)

# Add a font style and text
fontFace = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "openCV", (120,440), fontFace, 3, (0,230,0), 4,cv2.LINE_8)
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
# LineType = (FILLED, LINE_4: 4-connected line, LINE_8: 8-connected line, LINE_AA: antialiased line)


cv2.imshow('Window Title', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
