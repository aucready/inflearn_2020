from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬 푸시버튼")

        button = QtWidgets.QPushButton(self)
        button.setText('일반버튼')

        disableButton = QtWidgets.QPushButton(self)
        disableButton.setText('비활성버튼 ')
        disableButton.setEnabled(False)

        checkButton = QtWidgets.QPushButton(self)
        checkButton.setText('체크버튼')
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

# sys.exit(app.exec_())

