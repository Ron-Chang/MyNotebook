import cv2

cap = cv2.VideoCapture(0)
# cv2.VideoCapture('Filename.mov') to load a video.
# cv2.VideoCapture(Flage=integer)
# Flag = 0 or -1 means loading default camera, It's depending on your device.
# Flag = 1 to load secondary camera.

# Get properties width and height
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Assign the resolution to frameSize
frameSize = (cap_width,cap_height)

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
# It equals
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter("output.mov", fourcc, 20.0, frameSize)
# It equals
# out = cv2.VideoWriter()
# success = out.open("output.mov", fourcc, 20.0, frameSize,True)

# cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor)

# Make the video capture continue.
# Check the video is capable with isOpened()

if cap.isOpened():
    print("="*30+" CAMERA IS ON! "+"="*30)
    print("\nPress 'q' to stop recording.\n")

while cap.isOpened():
    ret, frame = cap.read()
    # type(cap.read()) = <class 'tuple'>
    # cap.read() = (True, array())

    if ret == True:
        # Write the frame into out
        out.write(frame)

        # Convert to grayscale video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cvtColor stand for convert to color
        # cv2.cvtColor(src, code, dst, dstCn)

        # Show the video
        cv2.imshow('Window Title', gray)

        # Once we pressed 'q' key then break while loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # ret is Fales
        # It means video has some loading issues, then we break loop
        break

print("="*29+" STOP RECORDING! "+"="*29)

cap.release()
out.release()
cv2.destroyAllWindows()
