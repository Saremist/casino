from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QSlider, QSpinBox
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
import sys


def guiMain(args):
    app = QApplication([])
    window = QWidget()
    slider = QSlider()
    spinbox = QSpinBox()
    layout = QVBoxLayout(window)
    layout.addWidget(slider)
    layout.addWidget(spinbox)
    
    def updateSpinbox(val):
        spinbox.setValue(val)

    def updateSlider(val):
        slider.setValue(val)

    slider.valueChanged.connect(updateSpinbox)
    spinbox.valueChanged.connect(updateSlider)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
