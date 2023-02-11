from PyQt5 import QtWidgets
from PyQt5 import QtCore


class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬GUI")

        button = QtWidgets.QPushButton(self)
        button.setText('파이썬 푸시버튼')

        disableButton = QtWidgets.QPushButton(self)
        disableButton.setText('비활성 버튼')
        disableButton.setEnabled(False)

        checkButton = QtWidgets.QPushButton(self)
        checkButton.setText('채트버튼')
        checkButton.setCheckable(True)
        checkButton.toggle()

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(button)
        layout.addWidget(disableButton)
        layout.addWidget(checkButton)

        self.setLayout(layout)
        self.show()

app = QtWidgets.QApplication([])
win = Mywindows()
app.exec_()
