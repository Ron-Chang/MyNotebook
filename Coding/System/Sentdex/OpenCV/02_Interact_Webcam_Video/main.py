import cv2
import numpy as np

# Display the video from the built-in camera
cap = cv2.VideoCapture(0)
# 0 - First (Default) Camera.
# 1 - Second etc.

# declare a codec
fourcc = cv2.VideoWriter_fourcc('j', 'p', 'e', 'g')
# note the lower case

# Get the camera properties
# https://blog.csdn.net/tuzixini/article/details/78847942
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# (w=1280, h=720) == (16:9)

# create a writer
out = cv2.VideoWriter("output.mov", fourcc, fps, size)

# Infinite Loop
while True:
    ret, frame = cap.read()
    # ret - return True or False

    # Convert BGR to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write frame into out
    out.write(frame)

    # Display Grayscale version
    cv2.imshow("GRAY", gray)

    # Terminate key binding
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
