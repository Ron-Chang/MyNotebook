'''
Tutorial 01 Application Structure

'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class Window(QMainWindow)






app = QApplication(sys.argv)
# Liststr = sys.argv
# app = PyQt5.QtWidgets.QApplication(Liststr)

window = QMainWindow()
"""
QtWidgets.QWidget(
    parent: QWidget,
    flags: UnionQt.WindowFlags,
    Qt.WindowType)
"""

window.setGeometry(500,250,480,200)
# setGeometry(postion_x, position_y, width, height)

window.setWindowTitle("PyQt Tutorials!")
# setWindowTitle("STRING")

#################################################
# above this line, this GUI is created in memory#
#################################################

window.show()
# showing the window to an user

sys.exit(app.exec_())
# Keep open the window until user close
