import cv2
import datetime
"""
datetime string format
https://www.jianshu.com/p/4b1836897272
"""

cap = cv2.VideoCapture(0)
# cv2.VideoCapture('Filename.mov') to load a video.
# cv2.VideoCapture(Flage=integer)
# Flag = 0 or -1 means loading default camera, It's depending on your device.
# Flag = 1 to load secondary camera.

# Get properties width and height
print("Original Width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Original Height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set property size
cap_width = 640
cap_height = 360
cap.set(3, cap_width)
cap.set(4, cap_height)
# cap.set(propId, value)
# propId 3 == width, 4 == height

print("Current Width:", cap_width)
print("Current Height:", cap_height)

if cap.isOpened():
    print("="*30+" CAMERA IS ON! "+"="*30)
    print("\nPress 'q' to stop monitoring.\n")

# Make the video capture continue.
# Check the video is capable with isOpened()
while cap.isOpened():
    ret, frame = cap.read()
    # type(cap.read()) = <class 'tuple'>
    # cap.read() = (True, array())

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text_1 = "Original_Size: " + str(cap.get(3)) + " X " + str(cap.get(4))
        text_2 = "Current_Size: " + str(cap_width) + " X " + str(cap_height)
        dt = datetime.datetime.now().strftime( '%Y-%m-%d %I:%M:%S %p' )

        frame = cv2.putText(frame, dt, (370, 30), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
        # cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
        frame = cv2.putText(frame, text_1, (30, 30), font, 0.6, (0, 224, 161), 1, cv2.LINE_AA)
        frame = cv2.putText(frame, text_2, (30, 50), font, 0.6, (0, 224, 161), 1, cv2.LINE_AA)


        # Show the video
        cv2.imshow('Window Title', frame)

        # Once we pressed 'q' key then break while loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # ret is Fales
        # It means video has some loading issues, then we break loop
        break

print("="*29+" STOP MONITORING! "+"="*29)

cap.release()
cv2.destroyAllWindows()
