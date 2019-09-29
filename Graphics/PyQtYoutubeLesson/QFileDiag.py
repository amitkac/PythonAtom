import sys
import os
from PyQt5.QtWidgets import (QPushButton, QHBoxLayout, QFileDialog,
                             QApplication, QWidget, QTextEdit, QVBoxLayout)


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clrBtn = QPushButton('clear')
        self.savBtn = QPushButton('save')
        self.openBtn = QPushButton('open')
        self.initUi()

    def initUi(self):
        vLayout = QVBoxLayout()  # vertical layout
        hLayout = QHBoxLayout()

        hLayout.addWidget(self.openBtn)
        hLayout.addWidget(self.savBtn)
        hLayout.addWidget(self.clrBtn)

        vLayout.addWidget(self.text)
        vLayout.addLayout(hLayout)

        self.setLayout(vLayout)
        self.setWindowTitle('Text Editor')
        self.clrBtn.clicked.connect(self.ClearTxt)
        self.savBtn.clicked.connect(self.saveTxt)
        self.openBtn.clicked.connect(self.openTxt)
        self.show()

    def ClearTxt(self):
        self.text.clear()

    def saveTxt(self):
        fname = QFileDialog.getSaveFileName(self, 'save file',
                                            os.getenv('HOME'))
        try:
            with open(fname[0], 'w') as fin:
                getText = self.text.toPlainText()
                fin.write(getText)
        except:
            # log exceptions here
            print('closing the window\n')
            pass

    def openTxt(self):
        fname = QFileDialog.getOpenFileName(self, 'open file',
                                            os.getenv('HOME'))
        try:
            with open(fname[0], 'r') as fin:
                fread = fin.read()
                self.text.setText(fread)
        except:
            pass


app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())
