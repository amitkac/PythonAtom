import sys
from PyQt5.QtWidgets import (QPushButton, QHBoxLayout,
                             QApplication, QWidget, QTextEdit)


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clrBtn = QPushButton('clear')
        self.savBtn = QPushButton('save')
        self.initUi()

    def initUi(self):
        layout = QHBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clrBtn)
        layout.addWidget(self.savBtn)

        self.setLayout(layout)
        self.setWindowTitle('Text Editor')
        self.clrBtn.clicked.connect(self.ClearTxt)
        self.savBtn.clicked.connect(self.saveTxt)
        self.show()

    def ClearTxt(self):
        self.text.clear()

    def saveTxt(self):
        with open('test.txt', 'w') as fin:
            getText = self.text.toPlainText()
            fin.write(getText)


app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())
