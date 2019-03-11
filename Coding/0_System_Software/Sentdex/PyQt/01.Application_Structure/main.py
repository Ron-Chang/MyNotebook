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
        self.setWindowTitle("PyQt Turtorial")
        self.setWindowIcon(QIcon("test.png"))
        self.show()

app = QApplication(sys.argv)
GUI = Window()

sys.exit(app.exec_())
