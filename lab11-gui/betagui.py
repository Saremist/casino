from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PySide2.QtWidgets import QHBoxLayout
import sys


def guiMain(args):
    app = QApplication(args)
    window = QWidget()
    
    address = QLineEdit()
    button = QPushButton("Go")
    layout = QHBoxLayout(window)
    layout.addWidget(address)
    layout.addWidget(button)
    window.show()
    return app.exec_()

guiMain(sys.argv)