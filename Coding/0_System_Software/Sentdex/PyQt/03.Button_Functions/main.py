'''
Tutorial 03 Button Functions

Customize button function

'''
import sys
from PyQt5.QtCore import QCoreApplication
# QCoreApplication is a module which is including button events

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial")
        self.setWindowIcon(QIcon("test.png"))
        # Above this line
        # Make a platform(It's a similar concept as 'composition' in AfterEffect)

        self.main_ui()
        # call user's own function main_ui()

    def main_ui(self):
        btn_quit = QPushButton("Quit",self)
        btn_quit.clicked.connect(self.close_application)
        btn_quit.resize(100,30)
        btn_quit.move(250,135)
        # print a default size
        print("btn_quit:"+str(btn_quit.sizeHint()))
        # set to a default size
        btn_quit.resize(btn_quit.sizeHint())

        btn_changeTitle = QPushButton("Change",self)
        btn_changeTitle.clicked.connect(self.changeTitle)
        btn_changeTitle.resize(100,30)
        btn_changeTitle.move(150,135)

        self.show()

    def changeTitle(self):
        window_title = self.windowTitle()
        # Get string from windowTitle()
        # (QWidget or QMainWindow).windowTitle()
        if window_title == "":
            self.setWindowTitle("PyQt Tutorial")
        else:
            self.setWindowTitle("")


    def close_application(self):
        sys.exit("Function has been terminated.")


def main():

    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


main()
