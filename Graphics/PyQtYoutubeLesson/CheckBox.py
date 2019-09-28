import sys
from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout,
                             QApplication, QWidget, QRadioButton)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        self.l2 = QLabel('who are you son?')
        self.dog = QRadioButton('Doggo')
        self.cat = QRadioButton('Kittu')
        self.b = QPushButton('pushy')
        # self.cbx = QCheckBox('are you human?')
        # self.l2.setPixmap(QtGui.QPixmap('google2.png'))

        # set layout
        # h_box = QHBoxLayout()
        # h_box.addStretch()
        # h_box.addWidget(self.l)
        # h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.l2)
        v_box.addWidget(self.dog)
        v_box.addWidget(self.cat)
        v_box.addWidget(self.b)
        # v_box.addLayout(h_box)
        # v_box.addWidget(self.l)

        self.setLayout(v_box)
        self.setWindowTitle('Radio Button')

        # slot is clicked--do the thing in fxn
        self.b.clicked.connect(lambda: self.btnClick(self.cat.isChecked()))
        # self.cbx.isChecked() is a signal

        self.show()

    def btnClick(self, chk):
        if chk:
            self.l2.setText('Meow Human')
        else:
            self.l2.setText('bowbow human')

            # It will change the text of the label l


app = QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())
