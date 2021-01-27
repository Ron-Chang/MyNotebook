import cv2
import numpy as np

ls = [[[1]],[[1]],[[1]],[[1]]]

arr = np.array(ls, np.uint8)



print(arr)
print(arr.shape)

g = np.random.randint(0,10, (250, 500), dtype=np.uint8)
b = np.random.randint(0,105, (250, 500), dtype=np.uint8)
r = np.random.randint(0,255, (250, 500), dtype=np.uint8)

img_1 = cv2.imread("../samples/3D-Matplotlib.png")

img=cv2.merge([b,g,r])

vis = cv2.subtract(img_1, img)
# vis2 = cv2.cvtColor(vis, cv2.COLOR_BGR2RGB)


cv2.imshow("ADD", vis)
cv2.moveWindow("ADD", 525, 20)

cv2.waitKey(0)
cv2.destroyAllWindows()
