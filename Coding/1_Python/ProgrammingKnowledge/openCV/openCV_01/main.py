import cv2

img = cv2.imread('sample.jpg', 0)
# cv2.imread(filename, flags)
# flags = 1 : Loads a color image
# flags = 0 : Loads image in grayscale mode
# flags = -1 : Loads image as such including alpha channel

print(img)
# If the file path is wrong, we'll get 'None'

cv2.imshow('image', img)
# cv2.imshow(winname, mat)

key = cv2.waitKey(0)
# cv2.waitKey(delay)
# 5000 == 5 secs
# 0 == keep running until pressd any key

if key == 27:
    cv2.destroyAllWindows()
    # or
    # cv2.destroyWindow(winname)
elif key == ord("s"):
    cv2.imwrite('sample_copy.jpg', img)
    # cv2.imwrite(filename, img, params)
    cv2.destroyAllWindows()
