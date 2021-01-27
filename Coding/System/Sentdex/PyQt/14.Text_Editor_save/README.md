# Tutorial 14 - PyQT Font widget -Save

#### 1.  增加`儲存行為`連接到`儲存程式`,加入到 `視窗標籤` 與 `工具欄`  

```python
# 開啟並讀取檔案
saveFile = QAction(QIcon("save.png"), ' &Save', self)
saveFile.setShortcut("Ctrl+S")
saveFile.setStatusTip("Save File")
saveFile.triggered.connect(self.file_save_as)

toolBar = self.addToolBar("MainToolBar")
toolBar.addAction(saveFile)

# 在主視窗加入menuBar命名為mainMenu
mainMenu = self.menuBar()
# 在mainMenu下建立File標籤，命名為fileMenu
fileMenu = mainMenu.addMenu(" &File")
fileMenu.addAction(saveFile)

# 啟動文字編輯器並置中
self.textEdit = QTextEdit()
self.setCentralWidget(self.textEdit)
# 啟用statusBar
self.statusBar()
#顯示視窗
self.show()
```
#### 2.  建立`儲存程式` 與容許取消  
```python
def file_save_as(self):
    try:
        # parent to self and the window title is "Save File"
        name = QFileDialog.getSaveFileName(self, "Save File")
        with open(name[0], "w") as file:
            text = self.textEdit.toPlainText()
            file.write(text)
    except Exception as Error_info:
        print(Error_info)
```
