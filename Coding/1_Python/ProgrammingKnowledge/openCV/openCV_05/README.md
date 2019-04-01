### Basic openCV - 05  
## Show date and time on videos  

### 1. Check openCV 02 to understand how to capture a video from camera  
[Basic openCV - 02](https://github.com/Ron-Chang/MyNotebook/tree/master/Coding/1_Python/ProgrammingKnowledge/openCV/openCV_02)  
```python
font = cv2.FONT_HERSHEY_SIMPLEX
text_1 = "Original_Size: " + str(cap.get(3)) + " X " + str(cap.get(4))
text_2 = "Current_Size: " + str(cap_width) + " X " + str(cap_height)
dt = datetime.datetime.now().strftime( '%Y-%m-%d %I:%M:%S %p' )

frame = cv2.putText(frame, dt, (370, 30), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
frame = cv2.putText(frame, text_1, (30, 30), font, 0.6, (0, 224, 161), 1, cv2.LINE_AA)
frame = cv2.putText(frame, text_2, (30, 50), font, 0.6, (0, 224, 161), 1, cv2.LINE_AA)
```
Reference:
[coreki - python的datetime](https://www.jianshu.com/p/4b1836897272)
