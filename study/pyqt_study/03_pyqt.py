from PyQt5 import QtWidgets
from PyQt5 import QtCore
class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('python gui')

        label1 = QtWidgets.QLabel('라벨1', self)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label1.resize(60, 30)

        label2 = QtWidgets.QLabel('라벨2', self)
        label2.setAlignment(QtCore.Qt.AlignRight)
        label2.setStyleSheet("color: red; font-size: 20px;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.show()

app = QtWidgets.QApplication([])
win = MyWindows()
app.exec()