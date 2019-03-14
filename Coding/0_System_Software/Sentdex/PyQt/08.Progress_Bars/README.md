# Tutorial 08 - Progressbar

#### 1. How to add Progressbar  
>PyQt5.QtWidgets.QProgressBar

###### 1. add a download button, and add a button shortcut.
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
        """What's the difference
        btn_doIt = QPushButton("Do it",self)
        btn_doIt.clicked.connect(self.download)
        btn_doIt.resize(200,60)
        btn_doIt.move(150,50)
        """

        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 110, 400, 20)

        self.btn_download = QPushButton("Download",self)
        # Add a button shortcut
        self.btn_download.setShortcut("Meta+D")
        self.btn_download.resize(200,60)
        self.btn_download.move(150,135)
        self.btn_download.clicked.connect(self.download)

        self.show()
```
###### 2. connect to download function which including progressbar

>#### 2. How to use Progressbar  
>PyQt5.QtCore.Qt.Checked  

```python
class Window(QMainWindow):

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.01

            self.progress.setValue(self.completed)
            percentage = "{:05.2f}".format(self.completed)+"\r"
            sys.stdout.write(percentage)
            sys.stdout.flush()
            if float(percentage.split("\r")[0]) == 100:
                self.downloadCompleted()
                self.setWindowTitle("DOWNLOADED!")
            else:
                self.setWindowTitle("downloading . . . ")
                """animation
                window_title = self.windowTitle()

                if window_title == "downloading ":
                    self.setWindowTitle("downloading . ")
                elif window_title == "downloading .":
                    self.setWindowTitle("downloading . . ")
                elif window_title == "downloading .":
                    self.setWindowTitle("downloading . . . ")
                else:
                    self.setWindowTitle("downloading ")
                """
```

The first parameter has to be `self` is needed. 
The second one `state` which could be any words, 
but it has to be match in the statement. 

#### 2. How to give a notice after download finished.

```python
class Window(QMainWindow):

    def downloadCompleted(self):
            completedNotice = QMessageBox.information(self, "completed", "Completed!")
```

__*Add an invisible shortcut*__  
```python
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial")

        # Add a invisible shortcut
        DownloadAction = QAction(" &Download", self)
        DownloadAction.setShortcut("Meta+D")
        DownloadAction.triggered.connect(self.download)
        self.addAction(DownloadAction)

```
