### Basic openCV - 04  
## Setting Camera Parameters  

### 1. Check openCV 02 to understand how to capture a video from camera  
[Basic openCV - 02](https://github.com/Ron-Chang/MyNotebook/tree/master/Coding/1_Python/ProgrammingKnowledge/openCV/openCV_02)  
```python
import cv2

cap = cv2.VideoCapture(0)
# cv2.VideoCapture('Filename.mov') to load a video.
# cv2.VideoCapture(Flage=integer)
# Flag = 0 or -1 means loading default camera, It's depending on your device.
# Flag = 1 to load secondary camera.

# Get properties width and height
print("original width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("original height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
```

### 2. Set width and height through `.set()` function  

```python
# Set property size
cap_width = 640
cap_height = 360
cap.set(3, cap_width)
cap.set(4, cap_height)
# cap.set(propId, value)
# propId 3 == width, 4 == height 
```

### 3. Set condition and make the video loop 
It's pretty similar way as [#02](https://github.com/Ron-Chang/MyNotebook/tree/master/Coding/1_Python/ProgrammingKnowledge/openCV/openCV_02), the only difference is without write in.

```python
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

print("="*29+" STOP MONITORING! "+"="*29)

cap.release()
cv2.destroyAllWindows()
```
