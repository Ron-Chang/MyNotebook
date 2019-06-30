import cv2
import numpy as np

# Display the video from the built-in camera
cap = cv2.VideoCapture(0)
# 0 - First (Default) Camera.
# 1 - Second etc.

# declare a codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter("output.mov", fourcc, 24, (1280,720),True)



# Infinite Loop
while True:
    ret, frame = cap.read()
    # ret - return True or False

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow("Gray", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
