import numpy as np
import cv2

# Check all Event Function
events = [i for i in dir(cv2) if "EVENT" in i]
print(events)
## equals
# events = []
# for i in dir(cv2):
#     if "EVENT" in i:
#         events.append(i)
# print(events)


def click_event(event, x, y, flags, param):
    # Everytime user click left button, show x,y values
    if event == cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+' , '+ str(y)
        print(text)

        # Refresh
        img = np.zeros((512,512,3), np.uint8)

        # make comma on the spot
        if x < 10:
            cv2.putText(img, text, (x-26, y-3), font, 0.6, (0, 224, 22), 1)
        elif x < 100:
            cv2.putText(img, text, (x-37, y-4), font, 0.6, (0, 224, 22), 1)
        else:
            cv2.putText(img, text, (x-49, y-4), font, 0.6, (0, 224, 22), 1)
        cv2.imshow("Window Title", img)

    elif event == cv2.EVENT_LBUTTONDOWN:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+' , '+ str(y)
        print(text)

        img = np.zeros((512,512,3), np.uint8)
        img = cv2.rectangle(img, (x-15, y-55), (x+15, y-25), (x*512/255,0,y*512/255), -1)

        # make comma on the spot
        if x < 10:
            cv2.putText(img, text, (x-26, y-3), font, 0.6, (x*512/255, 200, y*512/255), 1)
        elif x < 100:
            cv2.putText(img, text, (x-37, y-4), font, 0.6, (x*512/255, 200, y*512/255), 1)
        else:
            cv2.putText(img, text, (x-49, y-4), font, 0.6, (x*512/255, 200, y*512/255), 1)
        cv2.imshow("Window Title", img)

img = np.zeros((512,512,3), np.uint8)
cv2.imshow("Window Title", img)

cv2.setMouseCallback("Window Title", click_event)
# cv2.setMouseCallback(windowName, onMouse, param)

cv2.waitKey(0)
cv2.destroyAllWindows()
