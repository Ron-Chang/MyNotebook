'''
Tutorial 10 PyQT Font widget

add Font widget
excluded an issue about macOS can't change the font.
PyQt5 upgrade to 12.1 or downgrade to 10.1
'''

import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QProgressBar, QLabel, QComboBox, QSpacerItem, QFontDialog
from PyQt5.QtWidgets import QStyleFactory, QLabel, QComboBox, QMainWindow, QSizePolicy, QRadioButton
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt, QRect
from PyQt5.QtGui import *

class Winodw(QMainWindow):

    def __init__(self, parent=None):

        super(Winodw, self).__init__(parent)
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial 09")

        # 調用 FormWidget 進入MainWindow
        self.form_widget = FormWidget(self)

        self.setCentralWidget(self.form_widget)

        # 設定脫離行為
        extractAction = QAction(QIcon("exit.png"), " &Exit", self)
        extractAction.setShortcut("Shift+Q")
        extractAction.setStatusTip("Leave The Application")
        extractAction.triggered.connect(self.close_application)

        # 設定選擇字體
        fontChoice = QAction(QIcon("typography.png"), " &Font Style", self)
        fontChoice.setShortcut("Ctrl+F")
        fontChoice.setStatusTip("Change Font Styles")
        fontChoice.triggered.connect(self.fontChoice)
        # 啟動statusBar
        self.statusBar()

        # 在主視窗加入toolBar
        self.toolBar_MainToolBar = self.addToolBar("MainToolBar")

        # 在toolBar加入按鈕
        self.toolBar_MainToolBar.addAction(extractAction)

        # 獨立ToolBar for change font style
        self.toolBar_Edit = self.addToolBar("Edit")
        self.toolBar_Edit.addAction(fontChoice)

        self.Label_fontTest = QLabel('Change:\n0123456789')
        self.toolBar_Edit.addWidget(self.Label_fontTest)

        # 設定Main Menu
        mainMenu = self.menuBar()

        # 禁用原生MenuBar
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu(" &File")
        fileMenu.addAction(extractAction)

        # 設置無邊框視窗樣式
        self.setWindowFlags(Qt.FramelessWindowHint)
        #子視窗，視窗無按鈕 ，但有標題，可注釋掉觀察效果
        # self.setWindowFlags(Qt.SubWindow)

        #透過桌面模組得到屏幕的尺寸
        desktop=QApplication.desktop()
        #得到桌面可顯示的尺寸
        rect=desktop.availableGeometry()
        #設置視窗為屏幕可以顯示尺寸
        self.setGeometry(rect)
        #顯示視窗
        self.show()

    def fontChoice(self):
        font, valid = QFontDialog.getFont()
        print(font)
        if valid:
            self.Label_fontTest.setFont(font)

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

class FormWidget(QWidget):

    def __init__(self,parent):
        super(FormWidget, self).__init__(parent)
        #水平佈局
        self.Hlayout_1=QHBoxLayout()
        self.Hlayout_2=QHBoxLayout()
        self.Hlayout_3=QHBoxLayout()
        #垂直佈局
        self.Vlayout_1=QVBoxLayout()
        self.Vlayout_2=QVBoxLayout()
        self.Vlayout_3=QVBoxLayout()

        #實例化標籤與列表模組
        self.styleLabel_1=QLabel('Set Style')
        self.styleComboBox=QComboBox()

        #從QStyleFactory中增加多個顯示樣式到列表模組
        self.styleComboBox.addItems(QStyleFactory.keys())

        #選擇當前視窗的風格
        index=self.styleComboBox.findText(
            QApplication.style().objectName(),
            Qt.MatchFixedString
        )

        #設置當前視窗的風格
        self.styleComboBox.setCurrentIndex(index)

        #通過combobox模組選擇視窗風格
        self.styleComboBox.activated[str].connect(self.handlestyleChanged)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(0,0,10,10)

        # QRadioButton
        self.styleLabel_2=QLabel('Set Style')
        # self.styleLabel_2.setAlignment(Qt.AlignCenter)

        self.macintosh = QRadioButton(self)
        self.macintosh.setObjectName("macintosh")
        self.macintosh.setText("macintosh")
        self.windows = QRadioButton(self)
        self.windows.setObjectName("windows")
        self.windows.setText("windows")
        self.fusion = QRadioButton(self)
        self.fusion.setObjectName("fusion")
        self.fusion.setText("fusion")



        # 設定選擇字體
        self.btn_fontChoice = QPushButton(QIcon("typography.png"), "Font Style", self)
        self.btn_fontChoice.setShortcut("Ctrl+F")
        self.btn_fontChoice.clicked.connect(self.fontChoice)

        # Add a button shortcut
        self.btn_download = QPushButton("Download",self)
        self.btn_download.setShortcut("Meta+D")
        # self.btn_download.resize(200,60)
        # self.btn_download.move(150,135)
        self.btn_download.clicked.connect(self.download)

        # 空間排版物件
        spacerItem1 = QSpacerItem(0, 0,QSizePolicy.Expanding, QSizePolicy.Expanding)
        #QSizePolicy
        # - Fixed
        # - Minimum
        # - Maximum
        # - Preferred
        # - MinimumExpanding
        # - Expanding
        # - Ignored


        # 開始增加模組到主視窗，設置視窗佈置
        # 將視窗設定水平佈置
        self.setLayout(self.Hlayout_1)

        # 將Hlayout_1分為三份
        self.Hlayout_1.addLayout(self.Vlayout_1)
        self.Hlayout_1.addLayout(self.Vlayout_2)
        self.Hlayout_1.addLayout(self.Vlayout_3)

        # 在最左側的Vlayout_1加入QRadioButton
        self.Vlayout_1.addWidget(self.styleLabel_2)
        self.Vlayout_1.addWidget(self.macintosh)
        self.Vlayout_1.addWidget(self.windows)
        self.Vlayout_1.addWidget(self.fusion)
        # 在最左側的Vlayout_1加入spacerItem
        self.Vlayout_1.addItem(spacerItem1)
        self.Vlayout_1.addWidget(self.btn_fontChoice)

        # 在中間的Vlayout_2加入兩個水平佈置與一個spacerItem
        self.Vlayout_2.addLayout(self.Hlayout_2)
        self.Vlayout_2.addLayout(self.Hlayout_3)
        self.Vlayout_2.addItem(spacerItem1)

        # 在中間Vlayout_2最上方Hlayout_2左側加入文字標籤
        self.Hlayout_2.addWidget(self.styleLabel_1)
        # 在中間Vlayout_2最上方Hlayout_2右側加入ComboBox
        self.Hlayout_2.addWidget(self.styleComboBox)

        # 在中間Vlayout_2最下方Hlayout_3左側加入progressBar
        self.Hlayout_3.addWidget(self.progress)
        # 在中間Vlayout_2最下方Hlayout_3右側加入按鈕
        self.Hlayout_3.addWidget(self.btn_download)

        # 在最右側的Vlayout_3加入spacerItem
        self.Vlayout_3.addItem(spacerItem1)

    def fontChoice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleLabel_1.setFont(font)
            self.styleLabel_2.setFont(font)
            self.styleComboBox.setFont(font)

    #改變視窗風格
    def handlestyleChanged(self,style):
        QApplication.setStyle(style)
        print(QApplication.style().objectName(),
            Qt.MatchFixedString)

    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.1
            self.progress.setValue(self.completed)

    def downloadCompleted(self):
        completedNotice = QMessageBox.information(self, "completed", "Completed!")

app = QApplication([])
foo = Winodw()
foo.show()
sys.exit(app.exec_())
