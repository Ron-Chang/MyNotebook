# Tutorial 05 - Tool Bars

1. Understand how to addToolBar and QIcon
```python
'''
class Window(QMainWindow):

    def __init__(self):
        .
        .
        .
        self.main_ui()
        '''
    def main_ui(self):
        btn_quit = QPushButton("Quit",self)
        btn_quit.clicked.connect(self.close_application)
        btn_quit.resize(100,30)
        btn_quit.move(250,135)

        btn_changeTitle = QPushButton("Change",self)
        btn_changeTitle.clicked.connect(self.changeTitle)
        btn_changeTitle.resize(100,30)
        btn_changeTitle.move(150,135)

        extractAction = QAction(QIcon("exit.png"), "Exit the Function", self)
        extractAction.triggered.connect(self.close_application)
        # extractAction = triggered.connect(self.close_application())
        # It will activate close_application immediately

        extractAction = QAction(QIcon("exit.png"), "Exit the Function", self)
        extractAction.triggered.connect(self.close_application)

        openAction = QAction(QIcon("open.png"), "Open the File", self)
        openAction.triggered.connect(self.openFile)

        saveAction = QAction(QIcon("save.png"), "save the File", self)
        saveAction.triggered.connect(self.saveFile)

        changeAction = QAction(QIcon("settings.png"), "change the Window Title", self)
        changeAction.triggered.connect(self.changeTitle)

        self.toolBar = self.addToolBar("MainToolBar")

        self.toolBar.addAction(openAction)
        self.toolBar.addAction(saveAction)
        self.toolBar.addAction(changeAction)
        self.toolBar.addAction(extractAction)

        self.show()
```

