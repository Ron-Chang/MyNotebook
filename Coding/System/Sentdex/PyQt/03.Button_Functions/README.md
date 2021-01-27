# Tutorial 03 - Button Functions  
>Customize button function  

#### 1. Import QCoreApplication from QtCore, learn QtCore module
```python
import sys
from PyQt5.QtCore import QCoreApplication
# QCoreApplication is a module which is including button events
```
import the rest modules what we need
```python
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
```

#### 2. Create own function activate by click button, and get default button size  
```python
 class Window(QMainWindow):
    '''
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

        # print a default size in terminal (Optional)
        print("btn_quit:"+str(btn_quit.sizeHint()))
        # set to a default size
        btn_quit.resize(btn_quit.sizeHint())

    def close_application(self):
        sys.exit("Function has been terminated.")
        # quit("Function has been terminated.")
```

#### 3. Changing window title through to click a button.  
>If window title is an empty string, then assign "PyQt Tutorial", otherwise assign ""(an empty string).

```python
 class Window(QMainWindow):
    '''
    def __init__(self):
        .
        .
        .
    def close_application(self):
        sys.exit("Function has been terminated.")
    '''  
    def changeTitle(self):
        window_title = self.windowTitle()
        # Get string from windowTitle()
        # (QWidget or QMainWindow).windowTitle()
        if window_title == "":
            self.setWindowTitle("PyQt Tutorial")
        else:
            self.setWindowTitle("")
```

