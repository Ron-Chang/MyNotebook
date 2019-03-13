# Tutorial 07 - Checkbox

#### 1. How to add CheckBox  
>PyQt5.QtWidgets.QCheckBox  

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
    """
    btn_quit = QPushButton("Quit",self)
    ...
    btn_changeTitle.move(150,135)
    """
    checkBox = QCheckBox("Enlarge Window", self)
    checkBox.move(350,140)
    checkBox.resize(checkBox.sizeHint())
    checkBox.stateChanged.connect(self.enlargeWindow)
```

>#### 2. How to use CheckBox  
>PyQt5.QtCore.Qt.Checked  

```python
class Window(QMainWindow):

    def enlargeWindow(self, state):
        """
        The first parameter has to be self is needed.
        The second one is state and it could be any words,
        but it has to be match in the statement.
        """
        if state == Qt.Checked:
            self.setGeometry(100,100,800,600)
        else:
            self.setGeometry(100,100,500,300)
```

The first parameter has to be `self` is needed. 
The second one `state` which could be any words, 
but it has to be match in the statement. 

#### 2. How to make it toggle as the default state

```python
checkBox = QCheckBox("Enlarge Window", self)
checkBox.move(350,140)
checkBox.resize(checkBox.sizeHint())
checkBox.toggle()
checkBox.stateChanged.connect(self.enlargeWindow)
```
