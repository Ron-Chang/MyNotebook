# Tutorial 02 - Buttons  

#### 1. Introduce QtWidgets, QtCore and QtGui  
#### 2. The name rule of PyQt module
>PyQt5  
⎣_QtNames  
    ⎣_QModuleName  
        ⎣_functionName  

for instance:  
```python
PyQt5.QtWidgets.QWidget.setWindowTitle("String")  
```

#### 3. Understand the concept to using OOP to build GUI  
```python
class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Turtorial")
        self.setWindowIcon(QIcon("myicon.png"))
        # Above this line
        # Make a platform(It's a similar concept as 'composition' in AfterEffect)

        self.home()
        # call user's own function home()
```

#### 4.Create a build-in "Quit" function Button  
```python
class Window(QMainWindow):
    '''
    def __init__(self):
        .
        .
        .
        self.home()
    '''
    def home(self):
        btn = QPushButton("Quit",self)
        # PyQt5.QtWidgets.QPushButton("button_text",parent: QWidget)
        btn.clicked.connect(QCoreApplication.instance().quit)
        # Click Event
        # button.clicked.connect()

        # Default Quit Function
        # QCoreApplication.instance().quit

        btn.resize(100,30)
        # Give the button size
        btn.move(200,135)
        # Give the button position
        self.show()
```
```python
PushButton.clicked.connect(Event) # Event could be the function what we create

QCoreApplication.instance().quit # Default quit function
```

#### 5.Call the Gui  
```python

def main():

    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


main()
```
