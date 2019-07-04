import cv2
import numpy as np

img_1 = cv2.imread("../samples/3D-Matplotlib.png")
img_2 = cv2.imread("../samples/Basic-Plot.png")

python_logo = cv2.imread("../samples/python.png")

# unpack the python_logo info
# np.shape(foo) and foo.shape.
# see also: https://www.zhihu.com/question/38768460
rows, cols, channels = python_logo.shape
# np.shape = (rows=y, cols=x, each elements data depth)

roi = img_1[0:rows, 0:cols]
# From img_1 top-left(0) to bottom-left(rows), top-left(0) to top-right(cols)

# Convert the color to the grayscale
logo2gray = cv2.cvtColor(python_logo, cv2.COLOR_BGR2GRAY)

# 臨界值操作 https://blog.csdn.net/skeeee/article/details/9111139
ret, mask = cv2.threshold(logo2gray, 220, 255, cv2.THRESH_BINARY_INV)
# cv2.threshold(array, min_value, max_value, type)
# thresholdtype
# (THRESH_BINARY ,THRESH_BINARY_INV,THRESH_TRUNC,THRESH_TOZERO,THRESH_TOZERO_INV)

mask_inv = cv2.bitwise_not(mask)
# python logical "not", "and", "or" and "xor" etc.
img_1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img_2_fg = cv2.bitwise_and(python_logo, python_logo, mask=mask)

dst = cv2.add(img_1_bg, img_2_fg)
img_1[0:rows, 0:cols] = dst


# Add
add = cv2.add(img_1, img_2)
# [160, 120, 190] + [50, 180, 65] = [210, 300, 255] -> [210, 255, 255]

# 8 bit recuring add
recuring_add = img_1 + img_2
# [63, 0, 0] + [193, 256, 255] = [0, 0, 255]
# 256 -> 0, 260 -> 260-(255+1),we have to minus extra "1" because we count it from 0.
# 8 bit which can represent 0 to 255, there are 256 possibilities.
# cv2.add() will stop at 255, if the value is over the 255.

# Weighted Merge
weighted = cv2.addWeighted(img_1, 0.6, img_2, 0.4, 0)
# cv2.addWeighted(src1, alpha, src2, beta, gamma, dst, dtype)


cv2.imshow("ADD", add)
cv2.moveWindow("ADD", 525, 20)
cv2.imshow("RECURING ADD", recuring_add)
cv2.moveWindow("RECURING ADD", 525, 350)
cv2.imshow("WEIGHTED", weighted)
cv2.moveWindow("WEIGHTED", 525, 680)

cv2.imshow("IMG 1", img_1)
cv2.imshow("IMG 2", img_2)
cv2.moveWindow("IMG 1", 20, 20)
cv2.moveWindow("IMG 2", 20, 350)

cv2.waitKey(0)
cv2.destroyAllWindows()
