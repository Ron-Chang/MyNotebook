'''
Tutorial 12 PyQT Text Editor Widget

add text editor widget
'''

import sys
from PyQt5.QtCore import QCoreApplication, Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Winodw(QMainWindow):

    def __init__(self, parent=None):

        super(Winodw, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial 12")

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
        # ###########################

        # 在主視窗加入menuBar命名為mainMenu
        mainMenu = self.menuBar()
        # 在主視窗加入toolBar
        toolBar = self.addToolBar("MainToolBar")

        # 在toolBar加入行為[脫離]
        toolBar.addAction(extractAction)

        # 獨立ToolBar for change font style
        self.toolBar_Edit = self.addToolBar("Edit")
        self.toolBar_Edit.addAction(fontChoice)
        self.toolBar_Edit.addAction(fontBGColor)

        # 在mainMenu下建立File標籤，命名為fileMenu
        fileMenu = mainMenu.addMenu(" &File")
        # 在mainMenu下建立Edit標籤，命名為editMenu
        editMenu = mainMenu.addMenu(" &Edit")

        # File標籤下加入行為[脫離]
        fileMenu.addAction(extractAction)
        # Edit標籤下加入行為[選擇字體][設定背景顏色]
        editMenu.addAction(fontChoice)
        editMenu.addAction(fontBGColor)


        # # 設置無邊框視窗樣式
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # #子視窗，視窗無按鈕 ，但有標題，可注釋掉觀察效果
        # self.setWindowFlags(Qt.SubWindow)

        # #透過桌面模組得到屏幕的尺寸
        # desktop=QApplication.desktop()
        # #得到桌面可顯示的尺寸
        # rect=desktop.availableGeometry()
        # #設置視窗為屏幕可以顯示尺寸
        # self.setGeometry(rect)

        # 禁用原生MenuBar
        mainMenu.setNativeMenuBar(False)
        # 啟用statusBar
        self.statusBar()
        #顯示視窗
        self.show()

    def color_picker(self):
        color = QColorDialog.getColor()
        # self.styleLabel_1.setStyleSheet("QWidget { background-color: %s}" % color.name())
    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            pass

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
