'''
Tutorial 04 Main Menus

Customize button function

'''
import sys
from PyQt5.QtCore import QCoreApplication
# QCoreApplication is a module which is including button events

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QAction


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Turtorial")
        self.setWindowIcon(QIcon("test.png"))
        # Above this line
        # Make a platform(It's a similar concept as 'composition' in AfterEffect)
        extractAction = QAction(" &Exit", self)
        """What does “&” symbol mean in the name of menu bar?
        Check:
        https://stackoverflow.com/a/45093040
        It specifies the hot key or shortcut for the menu option.
        In the zetcode example, on Windows the Alt key activates the menu bar,
        and he uses &File, meaning Alt-F would select the file menu.
        The letter that follows the ampersand is the hot key.
        """

        """MacOS Keyword issue
        Check:
        http://zetcode.com/gui/pyqt5/menustoolbars/
        https://stackoverflow.com/a/45171461
        Easist way to fix it, use " &Exit" instead of "&Exit"

        or

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        """

        extractAction.setShortcut("Meta+Q")
        """MacOS Function Key
        ⌘Command: Ctrl
        ⌥Option: Alt
        ⌃Control: Meta
        ⇪Shift: Shift
        """


        extractAction.setStatusTip("Leave The Application")
        # Set status bar tips
        extractAction.triggered.connect(self.close_application)

        openAction = QAction(" &Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open File")
        openAction.triggered.connect(self.openFile)

        saveAction = QAction(" &Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save File")
        saveAction.triggered.connect(self.saveFile)

        saveAsAction = QAction(" &Save", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        saveAsAction.setStatusTip("Save as File")
        saveAsAction.triggered.connect(self.saveAsFile)

        changeTitleFunction = QAction(" &Change", self)
        changeTitleFunction.setShortcut("Meta+C")
        changeTitleFunction.setStatusTip("Change Window Title")
        changeTitleFunction.triggered.connect(self.changeTitle)

        self.statusBar()
        # Dispaly Status Bar at widow bottom
        # It show information everytime your mouse over the button which you "setStatusTip"

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        # Display the menu bar on windows, MacOS only

        fileMenu = mainMenu.addMenu(" &File")
        fileMenu.addAction(openAction)

        saveMenu = fileMenu.addMenu(" &Save")
        saveMenu.addAction(saveAction)
        saveMenu.addAction(saveAsAction)

        fileMenu.addAction(extractAction)
        fileMenu = mainMenu.addMenu(" &Edit")
        fileMenu.addAction(changeTitleFunction)

        self.main_ui()
        # call user's own function main_ui()

    def main_ui(self):
        btn_quit = QPushButton("Quit",self)
        btn_quit.clicked.connect(self.close_application)
        btn_quit.resize(100,30)
        btn_quit.move(250,135)

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
            self.setWindowTitle("PyQt Turtorial")
        else:
            self.setWindowTitle("")

    def openFile(self):
        print("Open? No, it won't happen right now.")

    def saveFile(self):
        print("Save? No, it won't happen right now.")

    def saveAsFile(self):
        print("Save as? No, it won't happen right now.")

    def close_application(self):
        sys.exit("Function has been terminated.")


def main():

    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


main()
