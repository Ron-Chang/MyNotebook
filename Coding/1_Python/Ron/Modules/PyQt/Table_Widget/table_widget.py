import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("Table Widget Exam")

        # 計次
        self.times = 1

        # 點擊後增加
        self.btn_add = QtWidgets.QPushButton("Push!", self)
        self.btn_add.clicked.connect(self.add_new_row)

        # 點擊後移除所選
        self.btn_remove = QtWidgets.QPushButton("Remove", self)
        self.btn_remove.clicked.connect(self.remove_row)

        # Set grid layout
        # grid = QtWidgets.QGridLayout()
        # self.setLayout(grid)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(5)

        # 隱藏垂直標籤
        # self.table.verticalHeader().setVisible(False)

        # 根據標籤寬度縮放
        self.table.resizeColumnsToContents()

        # 指定設置行寬
        self.table.setColumnWidth(2, 100)

        # 指定設置列高
        # self.table.setRowHeight(rowIndex, 24)

        # Row 分色
        self.table.setAlternatingRowColors(True)

        # 選擇整行
        self.table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        layout.addWidget(self.table)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_remove)



        self.show()

    def add_new_row(self):

        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        print("目前列數: {}".format(rowPosition+1))
        self.table.resizeColumnsToContents()

    def remove_row(self):

        row_index = self.table.currentRow()


        if row_index == -1:
            rowPosition = self.table.rowCount()
            print("為選擇,刪除最後一列,即第{}列: ".format(rowPosition))
            self.table.removeRow(rowPosition-1)
        else:
            print("刪除所選第{}列: ".format(row_index+1))
            self.table.removeRow(row_index)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
