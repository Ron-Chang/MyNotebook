'''
Tutorial 08 Progress Bar

add Shortcut
add Progress Bar
set Progress Bar position and size

'''
import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QMessageBox, QPushButton, QProgressBar
from PyQt5.QtWidgets import QWidget, QApplication, QAction


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("PyQt Tutorial")

        # Add a invisible shortcut
        # DownloadAction = QAction(" &Download", self)
        # DownloadAction.setShortcut("Meta+D")
        # DownloadAction.triggered.connect(self.download)
        # self.addAction(DownloadAction)

        self.main_ui()

    def main_ui(self):
        """What's the difference
        btn_doIt = QPushButton("Do it",self)
        btn_doIt.clicked.connect(self.download)
        btn_doIt.resize(200,60)
        btn_doIt.move(150,50)
        """

        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 110, 400, 20)

        self.btn_download = QPushButton("Download",self)
        # Add a button shortcut
        self.btn_download.setShortcut("Meta+D")
        self.btn_download.resize(200,60)
        self.btn_download.move(150,135)
        self.btn_download.clicked.connect(self.download)

        self.show()

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.01

            self.progress.setValue(self.completed)
            percentage = "{:05.2f}".format(self.completed)+"\r"
            sys.stdout.write(percentage)
            sys.stdout.flush()
            if float(percentage.split("\r")[0]) == 100:
                self.downloadCompleted()
                self.setWindowTitle("DOWNLOADED!")
            else:
                self.setWindowTitle("downloading . . . ")
                """animation
                window_title = self.windowTitle()

                if window_title == "downloading ":
                    self.setWindowTitle("downloading . ")
                elif window_title == "downloading .":
                    self.setWindowTitle("downloading . . ")
                elif window_title == "downloading .":
                    self.setWindowTitle("downloading . . . ")
                else:
                    self.setWindowTitle("downloading ")
                """

    def downloadCompleted(self):
        completedNotice = QMessageBox.information(self, "completed", "Completed!")



def main():

    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


main()
