### Basic openCV - 02
## How to read, write and show videos from camera in openCV

### 1. Import a video with `cv2.VideoCapture(Flag)`.  

```python
import cv2

cap = cv2.VideoCapture(0)
# cv2.VideoCapture('Filename.mov') to load a video.
# cv2.VideoCapture(Flage=integer)
# Flag = 0 or -1 means loading default camera, It's depending on your device.
# Flag = 1 to load secondary camera.
```
### 2. Get properties width and height and assign a new variable.  

```python
# Get properties width and height
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Assign the resolution to frameSize
frameSize = (cap_width,cap_height)
```

### 3.Get a codec from fourcc for write a video 

```python
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
# It equals
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")
```
### 4. Write a video to a file with `cv2.VideoWriter(filename,fourcc,fps,frameSize,isColor)`.  

isColor  
>If it is not zero, the encoder will expect and encode color frames,otherwise it will work with grayscale frames.  
*__(the flag is currently supported on `Windows` only)__*  

```python
out = cv2.VideoWriter("output.mov", fourcc, 20.0, frameSize)
# It equals
# out = cv2.VideoWriter()
# success = out.open("output.mov", fourcc, 20.0, frameSize,True)

# cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor)
```
### 5. Make the video capture continue and Check the video is capable with isOpened().  
```python
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
```
### 5. Release capturing, writing and closing all windows.  

```python
cap.release()
out.release()
cv2.destroyAllWindows()
```

### \#1 cv2.waitKey(delay) [From the doc](https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey)  

1.`waitKey(0)` will display the window `infinitely` until any keypress (it is suitable for image display).  

2.`waitKey(1)` will display a frame for `1 ms`, after which display will be automatically closed.  

So, if you use waitKey(0) you see a still image until you actually press something while for waitKey(1) the function will show a frame for 1 ms only.  


### \#2  `if cv2.waitKey(1) & 0xFF == ord('q'):`  

waitKey(1) 中的數字代表等待按鍵輸入之前的無效時間，單位為毫秒，在這個時間段內按鍵 ‘q’ 不會被記錄，在這之後按鍵才會被記錄，並在下一次進入if語段時起作用。也即經過無效時間以後，檢測在上一次顯示圖像的時間段內按鍵 ‘q’ 有沒有被按下，若無則跳出if語句段，捕獲並顯示下一幀圖像。

若此參數置零，則代表在捕獲並顯示了一幀圖像之後，程序將停留在if語句段中一直等待 ‘q’ 被鍵入。

cv2.waitKey(1) 與 0xFF（1111 1111）相與是因為cv2.waitKey(1) 的返回值不止8位，但是只有後8位實際有效，為避免產干擾，通過 ‘與’ 操作將其餘位置0。


Reference:  
[OpenCV Python Tutorial For Beginners](https://www.youtube.com/watch?v=TGQcDaZ56ao)  
[VideoCaptureProperties](https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d)  
[Difference in output with waitKey(0) and waitKey(1)](https://stackoverflow.com/a/51143586)  
weixin_42480593 - [if cv2.waitKey(1) & 0xFF == ord('q')分析](https://blog.csdn.net/weixin_42480593/article/details/82751180)  
[isColor](https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html)  
Supported Codec on macOS - [OpenCV Video Writer on Mac OS X](https://gist.github.com/takuma7/44f9ecb028ff00e2132e)  
