# 00 Intro - Basic GUI

GUI: Graphic User Interface
CLI: Command Line Interface


### Step 1  
```python
import sys
from PyQt5 import QtWidgets, QApplication
```

### Step 2
Call QtWidgets.QApplication(Liststr) as an app  




```python
app = QtWidgets.QApplication(sys.argv)
```

Call QtWidgets.QWidget(parent:QWidget, flags:UnionQt.WindowFlags, Qt.WindowType) as an window  
```python
window = QtWidgets.QWidget()
```

### Step 3
Set window's starting position and size  
setGeometry(postion_x, position_y, width, height)  
```python
window.setGeometry(500,250,480,200)
```

Set window's title  
setWindowTitle("STRING")  
```python
window.setWindowTitle("PyQt Tutorials!")
```

### Step 4
Call the GUI from memory to display
```python
window.show()
```

Keep app open, until user close it.
```pyhton
sys.exit(app.exec_())
```





<hr />  
###### What is `sys.argv`?  
>The name of the variable argv stands for "argument vector". A vector is a one-dimensional array, and argv is a one-dimensional array of strings.  

Basically, it's including path and name of itself as a first item of a list, then following with parameters.  
If we make a test file named `argv_test.py`.  
```python
import sys
foo = sys.argv[0:]
print(foo)
```
When you execute this file.  
`python3 argv_test.py --help -w abcdefg 12345`
>Result:  
['argv_test.py', '--help', '-w', 'abcdefg', '12345']  

The most important thing is those parameters is from another application.  
It's not associate with any codes from itself, except the first parameter `sys.argv[0]`.  
<hr />  

References:  
[python sys.argv 用法](https://www.itread01.com/content/1499953209.html)
