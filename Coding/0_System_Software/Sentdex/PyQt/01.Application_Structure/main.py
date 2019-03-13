'''
Tutorial 01 Application Structure

'''
import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial")
        # self.setWindowIcon(QIcon("myicon.icns"))
        self.show()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("myicon.icns"))
GUI = Window()

sys.exit(app.exec_())
