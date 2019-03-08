'''
Tutorial 01 Application Structure

'''
import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Turtorial")
        # self.setWindowIcon(QIcon("test.png"))
        self.show()

path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'test.png')
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(QPixmap(path)))
GUI = Window()

sys.exit(app.exec_())

# def _init_icon():
#     """Initialize the icon of qutebrowser."""
#     icon = QIcon()
#     fallback_icon = QIcon()
#     for size in [16, 24, 32, 48, 64, 96, 128, 256, 512]:
#         filename = ':/icons/qutebrowser-{}x{}.png'.format(size, size)
#         pixmap = QPixmap(filename)
#         qtutils.ensure_not_null(pixmap)
#         fallback_icon.addPixmap(pixmap)
#     qtutils.ensure_not_null(fallback_icon)
#     icon = QIcon.fromTheme('qutebrowser', fallback_icon)
#     qtutils.ensure_not_null(icon)
#     qApp.setWindowIcon(icon)

# sys.exit(app.exec_())
