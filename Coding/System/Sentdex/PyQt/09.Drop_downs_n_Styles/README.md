# Tutorial 09 - Drop down and Styles



#### 1. 增加下拉式列表  

```python
self.styleLabel_2=QLabel('Set Style ComboBox')
self.styleComboBox=QComboBox()

#從QStyleFactory中導入可用樣式到列表
self.styleComboBox.addItems(QStyleFactory.keys())
```
#### 2. 獲取支持系統預設風格  

```python
foo = PyQt5.QtWidgets.QStyleFactory.keys()
type(foo)
# result:
# <class 'list'>
print(foo)
# result(macOS):
# ['macintosh', 'Windows', 'Fusion']
```

#### 3. 獲取視窗尺寸,設置無邊窗
```python
# 設置無邊框視窗樣式
self.setWindowFlags(Qt.FramelessWindowHint)
#子視窗，視窗無按鈕 ，但有標題，可注釋掉觀察效果
# self.setWindowFlags(Qt.SubWindow)

#透過桌面模組得到屏幕的尺寸
desktop=QApplication.desktop()
#得到桌面可顯示的尺寸
rect=desktop.availableGeometry()
#設置視窗為屏幕可以顯示尺寸
self.setGeometry(rect)
#顯示視窗
self.show()
```
#### 4. 以comboBox為條件改變風格
```python
#選擇當前窗口的風格
index=self.styleComboBox.findText(
    QApplication.style().objectName(),
    Qt.MatchFixedString
)

#設置當前窗口的風格
self.styleComboBox.setCurrentIndex(index)

#通過combobox控件選擇窗口風格
self.styleComboBox.activated[str].connect(self.handlestyleChanged)

```
#### 5. 排版與空間物件  
```python
spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
#QSizePolicy
# - Fixed
# - Minimum
# - Maximum
# - Preferred
# - MinimumExpanding
# - Expanding
# - Ignored

# 開始增加控件到佈置，設置視窗佈置
# 將視窗設定水平佈置
self.setLayout(self.Hlayout_1)

# 將Hlayout_1分為三份
self.Hlayout_1.addLayout(self.Vlayout_1)
self.Hlayout_1.addLayout(self.Vlayout_2)
self.Hlayout_1.addLayout(self.Vlayout_3)

# 在最左側的Vlayout_1加入QRadioButton
self.Vlayout_1.addWidget(self.styleLabel_2)
self.Vlayout_1.addWidget(self.macintosh)
self.Vlayout_1.addWidget(self.windows)
self.Vlayout_1.addWidget(self.fusion)
# 在最左側的Vlayout_1加入spacerItem
self.Vlayout_1.addItem(spacerItem1)


# 在中間的Vlayout_2加入兩個水平佈置與一個spacerItem
self.Vlayout_2.addLayout(self.Hlayout_2)
self.Vlayout_2.addLayout(self.Hlayout_3)
self.Vlayout_2.addItem(spacerItem1)

# 在中間Vlayout_2最上方Hlayout_2左側加入文字標籤
self.Hlayout_2.addWidget(self.styleLabel_1)
# 在中間Vlayout_2最上方Hlayout_2右側加入ComboBox
self.Hlayout_2.addWidget(self.styleComboBox)

# 在中間Vlayout_2最下方Hlayout_3左側加入progressBar
self.Hlayout_3.addWidget(self.progress)
# 在中間Vlayout_2最下方Hlayout_3右側加入按鈕
self.Hlayout_3.addWidget(self.btn_download)

# 在最右側的Vlayout_3加入spacerItem
self.Vlayout_3.addItem(spacerItem1)
```
#### 5. 設置方程改變視窗風格
```python
# 對視窗風格屬性附值
def handlestyleChanged(self,style):
        QApplication.setStyle(style)
```


Reference:
[jia666666 - PyQt5圖形和特效之窗口風格（一）](https://blog.csdn.net/jia666666/article/details/81835851)
