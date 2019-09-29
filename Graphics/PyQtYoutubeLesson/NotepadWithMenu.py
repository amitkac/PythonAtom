import sys
import os
from PyQt5.QtWidgets import (QPushButton, QHBoxLayout, QFileDialog,
                             QApplication, QWidget, QTextEdit, QVBoxLayout,
                             QMainWindow, QAction, qApp)


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


class Writer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.formWidget = Notepad()
        self.setCentralWidget(self.formWidget)
        self.initUi()

    def initUi(self):
        bar = self.menuBar()

        # create Root Menu
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # create actions for menu
        saveAction = QAction('&Save', self)
        saveAction.setShortcut('Ctrl+s')

        newAction = QAction('&New', self)
        newAction.setShortcut('Ctrl+n')

        quitAction = QAction('&Quit', self)
        quitAction.setShortcut('Ctrl+q')

        openAction = QAction('&Open', self)
        openAction.setShortcut('Ctrl+o')

        findAction = QAction('Find...', self)
        replaceAction = QAction('Replace...', self)

        # add actions to menu
        file.addAction(newAction)
        file.addAction(saveAction)
        file.addAction(quitAction)
        file.addAction(openAction)

        # create sub menu
        findMenu = edit.addMenu('Find')
        findMenu.addAction(findAction)
        findMenu.addAction(replaceAction)

        # events
        quitAction.triggered.connect(self.quitTrigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle('Menu')
        self.resize(600, 400)
        self.show()

    def quitTrigger(self):
        qApp.quit()

    def selected(self, q):
        sig = q.text()

        if sig == 'New':
            self.formWidget.ClearTxt()
        elif sig == '&Open':
            self.formWidget.openTxt()
        elif sig == '&Save':
            self.formWidget.saveTxt()

        # print(q.text() + ' selected')


app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())
