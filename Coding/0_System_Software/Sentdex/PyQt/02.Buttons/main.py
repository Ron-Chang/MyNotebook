'''
Tutorial 02 Buttons

Make a 'Quit' button
Introduce QtWidgets, QtCore and QtGui

The name rule of PyQt5 module

PyQt5
⎣_QtNames
    ⎣_QModuleName
        ⎣_functionName
for instance:
PyQt5.QtWidgets.QWidget.setWindowTitle("String")

'''
import sys
from PyQt5.QtCore import QCoreApplication
# QCoreApplication is a module which is including button events

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, qApp


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Turtorial")
        # self.setWindowIcon(QIcon("myicon.png"))
        # Above this line
        # Make a platform(It's a similar concept as 'composition' in AfterEffect)

        self.home()
        # call user's own function home()

    def home(self):
        btn = QPushButton("Quit",self)
        # PyQt5.QtWidgets.QPushButton("button_text",parent: QWidget)
        btn.clicked.connect(QCoreApplication.instance().quit)
        # Click Event
        # button.clicked.connect()

        # Default Quit Function_1
        # QCoreApplication.instance().quit
        # Default Quit Function_2
        # qApp.quit

        btn.resize(100,30)
        # Give the button size
        btn.move(200,135)
        # Give the button position
        self.show()


def main():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("myicon.png"))
    GUI = Window()
    sys.exit(app.exec_())


main()
