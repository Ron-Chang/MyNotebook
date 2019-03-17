# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qt_Ui(object):
    def setupUi(self, qt_Ui):
        qt_Ui.setObjectName("qt_Ui")
        qt_Ui.resize(410, 286)
        qt_Ui.setWindowOpacity(0.95)
        self.verticalLayout = QtWidgets.QVBoxLayout(qt_Ui)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(qt_Ui)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_styleSet = QtWidgets.QLabel(self.frame)
        self.label_styleSet.setAlignment(QtCore.Qt.AlignCenter)
        self.label_styleSet.setObjectName("label_styleSet")
        self.verticalLayout_4.addWidget(self.label_styleSet)
        self.macintosh = QtWidgets.QRadioButton(self.frame)
        self.macintosh.setObjectName("macintosh")
        self.verticalLayout_4.addWidget(self.macintosh)
        self.windows = QtWidgets.QRadioButton(self.frame)
        self.windows.setObjectName("windows")
        self.verticalLayout_4.addWidget(self.windows)
        self.fusion = QtWidgets.QRadioButton(self.frame)
        self.fusion.setObjectName("fusion")
        self.verticalLayout_4.addWidget(self.fusion)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_styleList = QtWidgets.QLabel(qt_Ui)
        self.label_styleList.setObjectName("label_styleList")
        self.horizontalLayout_6.addWidget(self.label_styleList)
        self.comboBox = QtWidgets.QComboBox(qt_Ui)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(226, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_download = QtWidgets.QPushButton(qt_Ui)
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout_2.addWidget(self.pushButton_download)
        self.progressBar = QtWidgets.QProgressBar(qt_Ui)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(qt_Ui)
        QtCore.QMetaObject.connectSlotsByName(qt_Ui)

    def retranslateUi(self, qt_Ui):
        _translate = QtCore.QCoreApplication.translate
        qt_Ui.setWindowTitle(_translate("qt_Ui", "QT_test"))
        self.label_styleSet.setText(_translate("qt_Ui", "Style Set"))
        self.macintosh.setText(_translate("qt_Ui", "Macintosh"))
        self.windows.setText(_translate("qt_Ui", "Windows"))
        self.fusion.setText(_translate("qt_Ui", "Fusion"))
        self.label_styleList.setText(_translate("qt_Ui", "Style List"))
        self.comboBox.setItemText(0, _translate("qt_Ui", "macintosh"))
        self.comboBox.setItemText(1, _translate("qt_Ui", "windows"))
        self.comboBox.setItemText(2, _translate("qt_Ui", "fusion"))
        self.pushButton_download.setText(_translate("qt_Ui", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qt_Ui = QtWidgets.QWidget()
    ui = Ui_qt_Ui()
    ui.setupUi(qt_Ui)
    qt_Ui.show()
    sys.exit(app.exec_())

