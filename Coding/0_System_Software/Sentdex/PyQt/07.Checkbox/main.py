'''
Tutorial 07 Checkbox

add CheckBox
use CheckBox
toggle the CheckBox as default
'''
import sys
from PyQt5.QtCore import QCoreApplication, Qt
# QCoreApplication is a module which is including button events

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QApplication, QAction
from PyQt5.QtWidgets import QPushButton, QCheckBox


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial")
        self.setWindowIcon(QIcon("test.png"))

        extractAction = QAction(" &Exit", self)
        extractAction.setShortcut("Meta+Q")

        extractAction.setStatusTip("Leave The Application")
        extractAction.triggered.connect(self.close_application)

        openAction = QAction(" &Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open File")
        openAction.triggered.connect(self.openFile)

        saveAction = QAction(" &Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save File")
        saveAction.triggered.connect(self.saveFile)

        saveAsAction = QAction(" &Save As", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        saveAsAction.setStatusTip("Save as File")
        saveAsAction.triggered.connect(self.saveAsFile)

        changeTitleFunction = QAction(" &Change", self)
        changeTitleFunction.setShortcut("Meta+C")
        changeTitleFunction.setStatusTip("Change Window Title")
        changeTitleFunction.triggered.connect(self.changeTitle)

        self.statusBar()

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu(" &File")
        fileMenu.addAction(openAction)

        saveMenu = fileMenu.addMenu(" &Save")
        saveMenu.addAction(saveAction)
        saveMenu.addAction(saveAsAction)

        fileMenu.addAction(extractAction)
        fileMenu = mainMenu.addMenu(" &Edit")
        fileMenu.addAction(changeTitleFunction)

        self.main_ui()

    def main_ui(self):
        btn_quit = QPushButton("Quit",self)
        btn_quit.clicked.connect(self.close_application)
        btn_quit.resize(100,30)
        btn_quit.move(250,135)

        btn_changeTitle = QPushButton("Change",self)
        btn_changeTitle.clicked.connect(self.changeTitle)
        btn_changeTitle.resize(100,30)
        btn_changeTitle.move(150,135)

        checkBox = QCheckBox("Enlarge Window", self)
        checkBox.move(350,140)
        checkBox.resize(checkBox.sizeHint())
        # checkBox.toggle()
        checkBox.stateChanged.connect(self.enlargeWindow)

        self.show()

    def enlargeWindow(self, state):
        """
        The first parameter has to be self is needed.
        The second one is state and it could be any words,
        but it has to be match.in a condition statement.
        """
        if state == Qt.Checked:
            self.setGeometry(100,100,800,600)
        else:
            self.setGeometry(100,100,500,300)

    def changeTitle(self):
        window_title = self.windowTitle()

        if window_title == "":
            self.setWindowTitle("PyQt Turtorial")
        else:
            self.setWindowTitle("")

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
        choice = QMessageBox.question(self, "Extract!",
                                            "Are You Going to Leave Now?",
                                            QMessageBox.Yes | QMessageBox.No)
        """QMessageBox including
        question    For asking a question during normal operations.
        information For reporting information about normal operations.
        warning For reporting non-critical errors.
        critical    For reporting critical errors.
        """
        if choice == QMessageBox.Yes:
            print("Function has been terminated.")
            sys.exit()
        else:
            pass
            # do nothing


def main():

    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


main()
