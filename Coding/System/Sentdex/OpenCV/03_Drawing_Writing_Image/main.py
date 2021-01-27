import numpy as np
import cv2

img = cv2.imread("../samples/port.JPG", cv2.IMREAD_COLOR)

# A line
cv2.line(img, (0,0), (150,150), (255,0,0), 15)
cv2.line(img, (150,275), (400,275), (255,255,255), 40)
# cv2.line(image, start=(x1,y1), end=(x2,y2), color=(G,B,R), linewidth=int)

# A rectangle
cv2.rectangle(img, (150,150), (400,400), (0,255,0), 10)

# A circle
cv2.circle(img, (275,275), 125, (0, 0, 255), 10)
# cv2.circle(image, centre, radius, colour, linewidth)
# linewidth = -1 means fill the circle.

# A polygon
points = np.array([[225,400],[125,525],[425,525],[325,400]], np.int32)
# points = points.reshape((-1,1,2))
cv2.polylines(img, [points], False,(0,255,255) , 6)
# cv2.polylines(image, [points], Connect the ends, linewidth)

# A text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV Tuts!", (175, 285), font, 1, (255,0,255), 1, cv2.LINE_AA)
# cv2.putText(image,text,position,font,size,colour,thickness,line_type)

cv2.imshow("image", img)
# move the window to a specific position
cv2.moveWindow("image", 50, 50)
cv2.waitKey(0)
cv2.destroyAllWindows()

# https://blog.gtwang.org/programming/opencv-drawing-functions-tutorial/
