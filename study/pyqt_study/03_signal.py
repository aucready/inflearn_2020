from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys


class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬 푸시버튼")

        button1 = QtWidgets.QPushButton(self)
        button1.setText('버튼1')

        button2 = QtWidgets.QPushButton(self)
        button2.setText('버튼2')

        button1.clicked.connect(self.button_clicked)
        button2.clicked.connect(self.button_clicked)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)
        self.show()
    def button_clicked(self):
        sender = self.sender()
        QtWidgets.QMessageBox.about(self, '버튼테스트', sender.text())


app = QtWidgets.QApplication([])
win = Mywindows()
app.exec_()

# sys.exit(app.exec_())

