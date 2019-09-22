import sys
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.b = QtWidgets.QPushButton('pushy')
        self.l = QtWidgets.QLabel('I m not been clicked')
        self.l2 = QtWidgets.QLabel()
        self.l2.setPixmap(QtGui.QPixmap('google2.png'))

        # set layout
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)
        v_box.addWidget(self.l)
        v_box.addWidget(self.l2)

        self.setLayout(v_box)
        self.setWindowTitle('signals and slots')

        # slot is clicked--do the thing in fxn
        self.b.clicked.connect(self.btnClick)

        self.show()

    def btnClick(self):
        # It will change the text of the label l
        self.l.setText('yay! I got ckicked')


app = QtWidgets.QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())
