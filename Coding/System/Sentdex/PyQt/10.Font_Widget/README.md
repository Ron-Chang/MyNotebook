# Tutorial 10 - PyQT Font widget



#### 1. 設置按鈕呼叫預設字型視窗  

```python
self.btn_fontChoice = QPushButton(QIcon("typography.png"), "Font Style", self)
self.btn_fontChoice.setShortcut("Ctrl+F")
self.btn_fontChoice.clicked.connect(self.fontChoice)
```
#### 2. 執行並賦值  

呼叫預設字型視窗
PyQt5.QtWidgets.QFontDialog.getFont()

返回長度為2的列表
[記憶體座標(PyQt5.QtGui.QFont),是否改變(bool)]

```python
def fontChoice(self):
    font, valid = QFontDialog.getFont()
    if valid:
        self.styleLabel_1.setFont(font)
        self.styleLabel_2.setFont(font)
        self.styleComboBox.setFont(font)
```
