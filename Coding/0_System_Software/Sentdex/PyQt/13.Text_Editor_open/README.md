# Tutorial 13 - PyQT Font widget -Open  



#### 1.  增加`開啟行為`連接到`開啟程式`,加入到 `視窗標籤` 與 `工具欄`  

```python
# 開啟並讀取檔案
openFile = QAction(QIcon("open.png"), ' &Open File', self)
openFile.setShortcut("Ctrl+O")
openFile.setStatusTip("Load File")
openFile.triggered.connect(self.file_open)

toolBar = self.addToolBar("MainToolBar")
toolBar.addAction(openFile)

# 在主視窗加入menuBar命名為mainMenu
mainMenu = self.menuBar()
# 在mainMenu下建立File標籤，命名為fileMenu
fileMenu = mainMenu.addMenu(" &File")
fileMenu.addAction(openFile)

# 啟動文字編輯器並置中
self.textEdit = QTextEdit()
self.setCentralWidget(self.textEdit)
# 啟用statusBar
self.statusBar()
#顯示視窗
self.show()
```
#### 2.  建立`開啟程式` 與容許取消  
```python
def file_open(self):
    try:
        name = QFileDialog.getOpenFileName(self, "Open File") # parent to self and the window title is "Open File"
        file = open(name[0], "r")
        with file:
            text = file.read()
            self.textEdit.setText(text)
    except:
        pass
```

#### 3.  修正調色盤與字型程式  

```python
def color_picker(self):
    color = QColorDialog.getColor()
    if color.name() != "#000000":
        self.textEdit.setStyleSheet("QWidget { background-color: %s}" % color.name())
def font_choice(self):
    font, valid = QFontDialog.getFont()
    if valid:
        self.textEdit.setFont(font)
```
