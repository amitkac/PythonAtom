import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')

        # slider
        self.s1 = QtWidgets.QSlider(Qt.Horizontal)
        self.s1.setMinimum(0)
        self.s1.setMaximum(99)
        self.s1.setValue(0)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QtWidgets.QSlider.TicksBelow)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)

        self.setLayout(v_box)

        # same slot to two actions
        # slot is a function in reality

        # ----uncomment for a slot which uses only 1 information
        # self.b1.clicked.connect(self.btnClick)
        # self.b2.clicked.connect(self.btnClick)

        # to send more information, we have to use lambda functions
        self.b1.clicked.connect(lambda: self.btn_clk(self.b1, 'clear say'))
        self.b2.clicked.connect(lambda: self.btn_clk(self.b2, 'Print say'))
        self.s1.valueChanged.connect(self.valChange)
        self.show()

    def btnClick(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()

    def btn_clk(self, b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def valChange(self):
        myVal = str(self.s1.value())
        self.le.setText(myVal)


app = QtWidgets.QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())
