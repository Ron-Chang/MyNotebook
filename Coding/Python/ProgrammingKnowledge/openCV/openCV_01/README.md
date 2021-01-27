### Basic openCV - 01
## How to read, write and show images in openCV

### 1. Import a image with `cv2.imread(filename, flags)`.  

```python
import cv2

img = cv2.imread('sample.jpg', 0)
# cv2.imread(filename, flags)
# flags = 1 : Loads a color image
# flags = 0 : Loads image in grayscale mode
# flags = -1 : Loads image as such including alpha channel
```
### 2. Check the file path is avalible.  

```python
print(img)
# If the file path is wrong, we'll get 'None'
```

### 3. Show the image with `cv2.imshow(winname, mat)`.  

```python
cv2.imshow('image', img)
# cv2.imshow(winname, mat)
```
### 4. Keep the image open with `cv2.waitKey(delay)`.  
```python
key = cv2.waitKey(0)
# cv2.waitKey(delay)
# 5000 == 5 secs
# 0 == keep running until pressd any key
```
### 5. Set key to activate different behaviors.  
```python
if key == 27:
    cv2.destroyAllWindows()
    # or
    # cv2.destroyWindow(winname)
elif key == ord("s"):
    cv2.imwrite('sample_copy.jpg', img)
    # cv2.imwrite(filename, img, params)
    cv2.destroyAllWindows()
```

### \# openCV2 Keycodes

Key codes for OpenCV’s cv2.waitKey()

| Key           | Keycode              | Number   |
| ------------- | -------------------- | -------: |
| ESC           | keycode.KEY_ESCAPE   | 27       |
| Space         | keycode.KEY_SPACE    | 32       |
| Arrow Up      | keycode.KEY_UP       | 63232    |
| Arrow Down    | keycode.KEY_DOWN     | 63233    |
| Arrow Left    | keycode.KEY_LEFT     | 63234    |
| Arrow Right   | keycode.KEY_RIGHT    | 63235    |

### \# Non-Printable Key Codes  
For a good reference see [HERE](http://osxnotes.net/keybindings.html)  

|     key     |  code  |     key      |  code  | key |  code  |
|-------------|--------|--------------|--------|-----|--------|
| Up Arrow    | \UF700 | Backspace    | \U0008 | F1  | \UF704 |
| Down Arrow  | \UF701 | Tab          | \U0009 | F2  | \UF705 |
| Left Arrow  | \UF702 | Enter        | \U000A | F3  | \UF706 |
| Right Arrow | \UF703 | Escape       | \U001B | ... |        |
| Insert      | \UF727 | Page Up      | \UF72C |     |        |
| Delete      | \UF728 | Page Down    | \UF72D |     |        |
| Home        | \UF729 | Print Screen | \UF72E |     |        |
| End         | \UF72B | Scroll Lock  | \UF72F |     |        |
| SysReq      | \UF731 | Pause        | \UF730 |     |        |
| Break       | \UF732 | Menu         | \UF735 |     |        |
| Help        | \UF746 | Delete       | \U007F |     |        |


Reference:  
[OpenCV Python Tutorial For Beginners](https://www.youtube.com/watch?v=TGQcDaZ56ao)  
[HHG-Analysis-Python 0.8 documentation](http://pklaus.github.io/HHG-Analysis-Python/helpers.html#module-keycode)  
[trusktr/macOS keybinding.dict](https://gist.github.com/trusktr/1e5e516df4e8032cbc3d)  
