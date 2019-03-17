import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QProgressBar, QLabel, QComboBox
from PyQt5.QtWidgets import QStyleFactory, QLabel, QComboBox, QMainWindow, QSizePolicy, QRadioButton
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QHBoxLayout, QSpacerItem, QVBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import *

class Winodw(QMainWindow):

    def __init__(self, parent=None):

        super(Winodw, self).__init__(parent)
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial")

        self.form_widget = FormWidget(self)

        self.setCentralWidget(self.form_widget)

        # 設定脫離行為
        extractAction = QAction(QIcon("exit.png"), " &Exit", self)
        extractAction.setShortcut("Shift+Q")
        extractAction.setStatusTip("Leave The Application")
        extractAction.triggered.connect(self.close_application)

        # 啟動statusBar
        self.statusBar()

        # 在主視窗加入toolBar
        self.toolBar = self.addToolBar("MainToolBar")

        # 在toolBar加入脫離按鈕
        self.toolBar.addAction(extractAction)

        # 設定Main Menu
        mainMenu = self.menuBar()

        #禁用原生MenuBar
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu(" &File")
        fileMenu.addAction(extractAction)

        # 設置無邊框窗口樣式
        # self.setWindowFlags(Qt.FramelessWindowHint)
        #子窗口，窗口無按鈕 ，但有標題，可注釋掉觀察效果
        # self.setWindowFlags(Qt.SubWindow)

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

    def __init__(self,parent=None):
        super(FormWidget, self).__init__(parent)
        #水平佈局
        self.Hloyout_1=QHBoxLayout()
        self.Hloyout_2=QHBoxLayout()
        self.Hloyout_3=QHBoxLayout()
        self.Vloyout_1=QVBoxLayout()
        self.Vloyout_2=QVBoxLayout()
        self.Vloyout_3=QVBoxLayout()

        #實例化標籤與列表控件
        self.styleLabel_2=QLabel('Set Style ComboBox')
        self.styleComboBox=QComboBox()

        #從QStyleFactory中增加多個顯示樣式到列表控件
        self.styleComboBox.addItems(QStyleFactory.keys())

        #選擇當前窗口的風格
        index=self.styleComboBox.findText(
            QApplication.style().objectName(),
            Qt.MatchFixedString
        )

        #設置當前窗口的風格
        self.styleComboBox.setCurrentIndex(index)

        #通過combobox控件選擇窗口風格
        self.styleComboBox.activated[str].connect(self.handlestyleChanged)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(0,0,10,10)

        '''QRadioButton
        self.styleLabel_1=QLabel('Set Style')
        self.styleLabel_1.setAlignment(Qt.AlignCenter)
        self.macintosh = QRadioButton(self)
        self.macintosh.setObjectName("macintosh")
        self.macintosh.setText("macintosh")
        self.windows = QRadioButton(self)
        self.windows.setObjectName("windows")
        self.windows.setText("windows")
        self.fusion = QRadioButton(self)
        self.fusion.setObjectName("fusion")
        self.fusion.setText("fusion")
        '''

        # Add a button shortcut
        self.btn_download = QPushButton("Download",self)
        self.btn_download.setShortcut("Meta+D")
        # self.btn_download.resize(200,60)
        # self.btn_download.move(150,135)
        self.btn_download.clicked.connect(self.download)

        spacerItem1 = QSpacerItem(0, 40,QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacerItem2 = QSpacerItem(226, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #QSizePolicy
        # - Fixed
        # - Minimum
        # - Maximum
        # - Preferred
        # - MinimumExpanding
        # - Expanding
        # - Ignored

        # 添加控件到佈局，設置窗口佈局
        self.Vloyout_1.addItem(spacerItem2)
        '''QRadioBox
        self.Vloyout_1.addWidget(self.macintosh)
        self.Vloyout_1.addWidget(self.windows)
        self.Vloyout_1.addWidget(self.fusion)
        self.Vloyout_1.addItem(spacerItem1)
        '''

        self.Hloyout_1.addLayout(self.Vloyout_1)
        self.Hloyout_1.addLayout(self.Vloyout_2)
        self.Hloyout_1.addLayout(self.Vloyout_3)

        self.Vloyout_2.addLayout(self.Hloyout_2)
        self.Vloyout_2.addLayout(self.Hloyout_3)
        self.Vloyout_2.addItem(spacerItem1)


        self.Hloyout_2.addWidget(self.styleLabel_2)
        self.Hloyout_2.addWidget(self.styleComboBox)

        self.Hloyout_3.addWidget(self.progress)
        self.Hloyout_3.addWidget(self.btn_download)

        self.Vloyout_3.addItem(spacerItem2)

        self.setLayout(self.Hloyout_1)

    #改變窗口風格
    def handlestyleChanged(self,style):
        QApplication.setStyle(style)

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

