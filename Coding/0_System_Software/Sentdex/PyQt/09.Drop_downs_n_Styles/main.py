import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QProgressBar, QLabel, QComboBox
from PyQt5.QtWidgets import QStyleFactory, QLabel, QComboBox, QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import *

class Winodw(QMainWindow):

    def __init__(self, parent=None):

        super(Winodw, self).__init__(parent)
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial")

        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)
        # # 設置無邊框窗口樣式
        self.setWindowFlags(Qt.FramelessWindowHint)
        # #子窗口，窗口無按鈕 ，但有標題，可注釋掉觀察效果
        # self.setWindowFlags(Qt.SubWindow)


class FormWidget(QWidget):

    def __init__(self,parent=None):
        super(FormWidget, self).__init__(parent)
        #水平佈局
        Hloyout=QHBoxLayout()

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

