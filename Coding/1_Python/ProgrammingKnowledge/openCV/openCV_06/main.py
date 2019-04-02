import numpy as np

import cv2

# Check all Event Function
events = [i for i in dir(cv2) if "EVENT" in i]
## equals
# events = []

# for i in dir(cv2):
#     if "EVENT" in i:
#         events.append(i)

print(events)


def click_event(event, x, y, flags, param):
    # Everytime user click left button, show x,y values
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_1 = str(x),', ', str(y)
        img = np.zeros((512,512,3))
        cv2.putText(img, text_1, (x, y), font, 1, (255,255,0), 1, cv2.LINE_AA)
        cv2.imshow("IMAGE", img)

img = np.zeros((512,512,3))
cv2.imshow("IMAGE", img)

cv2.setMouseCallback("IMAGE", click_event)
# cv2.setMouseCallback(windowName, onMouse, param)

cv2.waitKey(0)
cv2.destroyAllWindows()
