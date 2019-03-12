# Tutorial 05 - Tool Bars

1. Create "Exit" in "File" main menus
```python
'''
class Window(QMainWindow):

    def __init__(self):
        .
        .
        .
        self.setWindowIcon(QIcon("test.png"))
        '''
        extractAction = QtGui.QAction("&Let's Get Out Of Here!",self)
        extractAction.setShortcut("Command+T")
        extractAction.setStatusTip("Leave The Application") 
        # Set status bar tips
        
        extractAction.triggered.connect(self.close_application)
        self.statusBar() 
        # Dispaly Status Bar

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
```

