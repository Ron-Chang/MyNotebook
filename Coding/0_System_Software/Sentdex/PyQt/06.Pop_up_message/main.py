'''
Tutorial 06 Pop up Message

Make pop up message

'''
import sys
from PyQt5.QtCore import QCoreApplication
# QCoreApplication is a module which is including button events

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QApplication, QPushButton, QAction


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Turtorial")
        self.setWindowIcon(QIcon("test.png"))

        extractAction = QAction(" &Exit", self)
        extractAction.setShortcut("Meta+Q")
        """MacOS Function Key
        ⌘Command: Ctrl
        ⌥Option: Alt
        ⌃Control: Meta
        ⇪Shift: Shift
        """

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

        extractAction = QAction(QIcon("exit.png"), "Exit the Function", self)
        extractAction.triggered.connect(self.close_application)
        # extractAction = triggered.connect(self.close_application())
        # It will activate close_application immediatly

        extractAction = QAction(QIcon("exit.png"), "Exit the Function", self)
        extractAction.triggered.connect(self.close_application)

        openAction = QAction(QIcon("open.png"), "Open the File", self)
        openAction.triggered.connect(self.openFile)

        saveAction = QAction(QIcon("save.png"), "save the File", self)
        saveAction.triggered.connect(self.saveFile)

        changeAction = QAction(QIcon("settings.png"), "change the Window Title", self)
        changeAction.triggered.connect(self.changeTitle)

        self.toolBar = self.addToolBar("MainToolBar")

        self.toolBar.addAction(openAction)
        self.toolBar.addAction(saveAction)
        self.toolBar.addAction(changeAction)
        self.toolBar.addAction(extractAction)

        self.show()

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
        """QMessageBox includin
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
