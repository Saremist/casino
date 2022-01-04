from PySide2.QtWidgets import QApplication
# from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QMainWindow#, QWidget
import sys
from ui_airquality import Ui_MainWindow


class AirQualityWindow(QMainWindow):
    def init(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def guiMain(args):
    app = QApplication(args)
    window = AirQualityWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
