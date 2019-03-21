# Tutorial 10 - PyQT Font widget



#### 1. 設置按鈕呼叫預設選色器  

```python
# Set Default Color is black R,G,B == 0,0,0
color = QColor(0,0,0)
btn_fontColor = QPushButton('BG Color', self)
btn_fontColor.setShortcut("Shift+P")
btn_fontColor.clicked.connect(self.color_picker)
```
#### 2. 執行並賦值  

呼叫預設字型視窗
QColorDialog.getColor()

color = QColorDialog.getColor()
color.name() 返回值格式 #000000

```python
def color_picker(self):
        color = QColorDialog.getColor()
        self.styleLabel_1.setStyleSheet("QWidget { background-color: %s}" % color.name())
        self.styleLabel_2.setStyleSheet("QWidget { background-color: %s}" % color.name())
```
#### 3. 呼叫預設日曆

```python
cal = QCalendarWidget(self)
cal.resize(200,200)
```
