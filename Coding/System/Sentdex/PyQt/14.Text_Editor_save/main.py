'''
Tutorial 13 PyQT Text Editor Widget -Open

add open file function
'''

import sys
from PyQt5.QtCore import QCoreApplication, Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Winodw(QMainWindow):

    def __init__(self, parent=None):

        super(Winodw, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial 13")

        # ######### 設定行為 #########
        # 脫離
        extractAction = QAction(QIcon("exit.png"), " &Exit", self)
        extractAction.setShortcut("Shift+Q")
        extractAction.setStatusTip("Leave The Application")
        extractAction.triggered.connect(self.close_application)
        # 選擇字體
        fontChoice = QAction(QIcon("typography.png"), " &Font", self)
        fontChoice.setShortcut("Shift+P")
        fontChoice.setStatusTip("Change Font Styles")
        fontChoice.triggered.connect(self.font_choice)
        # 設定背景顏色
        color = QColor(0,0,0) #預設為黑色
        fontBGColor = QAction(QIcon("settings.png"), ' &BGC', self)
        fontBGColor.setShortcut("Shift+C")
        fontBGColor.setStatusTip("Change Font Background Color")
        fontBGColor.triggered.connect(self.color_picker)
        # 開啟並讀取檔案
        openFile = QAction(QIcon("open.png"), ' &Open File', self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Load File")
        openFile.triggered.connect(self.file_open)
        # 儲存檔案
        saveFile = QAction(QIcon("save.png"), ' &Save', self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("Save File")
        saveFile.triggered.connect(self.file_save_as)
        # ###########################

        # 在主視窗加入menuBar命名為mainMenu
        mainMenu = self.menuBar()
        # 在mainMenu下建立File標籤，命名為fileMenu
        fileMenu = mainMenu.addMenu(" &File")
        # 在mainMenu下建立Edit標籤，命名為editMenu
        editMenu = mainMenu.addMenu(" &Edit")
        # File標籤下加入行為[開啟並讀取檔案] [脫離] [選擇字體] [設定背景顏色]
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(extractAction)
        # Edit標籤下加入行為[選擇字體][設定背景顏色]
        editMenu.addAction(fontChoice)
        editMenu.addAction(fontBGColor)

        # 在主視窗加入toolBar
        toolBar = self.addToolBar("MainToolBar")
        # 在toolBar加入行為[脫離]
        toolBar.addAction(openFile)
        toolBar.addAction(saveFile)
        toolBar.addAction(fontChoice)
        toolBar.addAction(fontBGColor)
        toolBar.addAction(extractAction)

        # # 設置無邊框視窗樣式
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # #子視窗，視窗無按鈕 ，但有標題，可注釋掉觀察效果
        # self.setWindowFlags(Qt.SubWindow)

        # 啟動文字編輯器並置中
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # 禁用原生MenuBar
        mainMenu.setNativeMenuBar(False)

        # #透過桌面模組得到屏幕的尺寸
        # desktop=QApplication.desktop()
        # #得到桌面可顯示的尺寸
        # rect=desktop.availableGeometry()
        # #設置視窗為屏幕可以顯示尺寸
        # self.setGeometry(rect)
        # 啟用statusBar
        self.statusBar()
        #顯示視窗
        self.show()

    def file_open(self):
        try:
            # parent to self and the window title is "Open File"
            name = QFileDialog.getOpenFileName(self, "Open File")
            with open(name[0], "r") as file:
                text = file.read()
                self.textEdit.setText(text)
        except Exception as Error_info:
            print(Error_info)

    def file_save_as(self):
        try:
            # parent to self and the window title is "Save File"
            name = QFileDialog.getSaveFileName(self, "Save File")
            with open(name[0], "w") as file:
                text = self.textEdit.toPlainText()
                file.write(text)
        except Exception as Error_info:
            print(Error_info)

    def color_picker(self):
        color = QColorDialog.getColor()
        if color.name() != "#000000":
            self.textEdit.setStyleSheet("QWidget { background-color: %s}" % color.name())
    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.textEdit.setFont(font)
    def close_application(self):
        choice = QMessageBox.question(self, "Extract!",
                                            "Are You Going to Leave Now?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Function has been terminated.")
            sys.exit()
        else:
            pass
            # do nothing


app = QApplication([])
GUI = Winodw()
GUI.show()
sys.exit(app.exec_())
