# Tutorial 06 -  Pop up Message

1. Understand how to addToolBar
```python
'''
class Window(QMainWindow):

    def __init__(self):
        .
        .
        .
    def changeTitle(self):
        window_title = self.windowTitle()

        if window_title == "":
            self.setWindowTitle("PyQt Tutorial")
        else:
            self.setWindowTitle("")
        '''
    def openFile(self):
        openAction = QMessageBox.information(self, "openFile",
                                            "Open a file?\n"+
                                            "I'm sorry, it won't happen right now.")
    def saveFile(self):
        openAction = QMessageBox.warning(self, "saveFile",
                                            "Save a file?\n"+
                                            "I'm sorry, it won't happen right now.")

    def saveAsFile(self):
        openAction = QMessageBox.critical(self, "openAsFile",
                                            "Save as to?\n"+
                                            "I'm sorry, it won't happen right now.")
    def close_application(self):
        choice = QMessageBox.warning(self, "Extract!",
                                            "Are You Going to Leave Now?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Function has been terminated.")
            sys.exit()
        else:
            pass
            # do nothing
```
>PyQt5.QtGui.QMessageBox( ) defined icon  

|         Type        |   Keyword   |                      Function                      |
|---------------------|-------------|----------------------------------------------------|
| ![quest](quest.png) | question    | For asking a question during normal operations.    |
| ![info](info.png)   | information | For reporting information about normal operations. |
| ![warn](warn.png)   | warning     | For reporting non-critical errors.                 |
| ![crit](crit.png)   | critical    | For reporting critical errors.                     |
|                     |             |                                                    |
