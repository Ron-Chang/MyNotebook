# Tutorial 04 - Main Menus

#### 1. Create "Exit" in "File" main menus
```python
'''
class Window(QMainWindow):

    def __init__(self):
        .
        .
        .
        self.setWindowIcon(QIcon("test.png"))
        '''
        extractAction = QAction(" &Exit", self)
        extractAction.setShortcut("Meta+Q")
        extractAction.setStatusTip("Leave The Application")
        # Set status bar tips
        
        extractAction.triggered.connect(self.close_application)
        
        self.statusBar() 
        # Dispaly Status Bar
        # It show information everytime your mouse over the button which you "setStatusTip"

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
```

#### 2. What does “&” symbol mean in the name of menu bar?  
>It specifies the hot key or shortcut for the menu option.
In the zetcode example, on Windows the Alt key activates the menu bar,
and he uses &File, meaning Alt-F would select the file menu.
The letter that follows the ampersand is the hot key.

Check here:  
[stackoverflow-45093040](https://stackoverflow.com/a/45093040)  

#### 3. MacOS Keyword issue  
>Easist way to fix it, use " &Exit" instead of "&Exit"  
or  
mainMenu = self.menuBar()  
mainMenu.setNativeMenuBar(False)  

Check here:  
[zetcode/menustoolbars](http://zetcode.com/gui/pyqt5/menustoolbars)  
[stackoverflow-45171461](https://stackoverflow.com/a/45171461)  

#### 4. Set Shortcut with MacOS Function Key  

`extractAction.setShortcut("Meta+Q")`  
__*Beware of case sensitive*__  

|    Mac    |  pyqt |
|-----------|-------|
| ⌘ Command | Ctrl  |
| ⌥ Option  | Alt   |
| ⌃ Control | Meta  |
| ⇪ Shift   | Shift |

#### 5. What is statusBar?  
Dispaly Status Bar at widow bottom. It shows information if your mouse overed the button.


#### 6. Add `save` and `save As` into `Save` menu in `File` menu
`File`  
- ⎣`Save`  
- - ⎜Save  
- - ⎣Save As  


```python
saveAction = QAction(" &Save", self)
saveAction.setShortcut("Ctrl+S")
saveAction.setStatusTip("Save File")
saveAction.triggered.connect(self.saveFile)

saveAsAction = QAction(" &Save", self)
saveAsAction.setShortcut("Ctrl+Shift+S")
saveAsAction.setStatusTip("Save as File")
saveAsAction.triggered.connect(self.saveAsFile)
# Create save Save action and Save As action


fileMenu = mainMenu.addMenu(" &File")
# Create File menu, this is belonging to mainMenu = self.menuBar()

saveMenu = fileMenu.addMenu(" &Save")
# Create Save menu make it belonging to fileMenu
saveMenu.addAction(saveAction)
saveMenu.addAction(saveAsAction)
# Add Save action and Save As action into Save menu
```
