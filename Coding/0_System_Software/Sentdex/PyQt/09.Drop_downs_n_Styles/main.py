import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QProgressBar, QLabel, QComboBox
from PyQt5.QtWidgets import QStyleFactory, QLabel, QComboBox, QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QHBoxLayout, QVBoxLayout
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
        Hloyout=QHBoxLayout()
        Vloyout=QVBoxLayout()

        #實例化標籤與列表控件
        self.styleLabel=QLabel('Set Style')
        self.styleComboBox=QComboBox()

        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 110, 400, 20)
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

        # 添加控件到佈局，設置窗口佈局

        Hloyout.addWidget(self.styleLabel)
        Hloyout.addWidget(self.styleComboBox)
        Hloyout.addWidget(self.progress)
        self.setLayout(Hloyout)



    #改變窗口風格
    def handlestyleChanged(self,style):
        QApplication.setStyle(style)

    def downloadCompleted(self):
        completedNotice = QMessageBox.information(self, "completed", "Completed!")

app = QApplication([])
foo = Winodw()
foo.show()
sys.exit(app.exec_())

