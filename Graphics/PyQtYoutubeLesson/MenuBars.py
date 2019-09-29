import sys
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QFileDialog, QAction,
                             qApp, QApplication, QWidget, QTextEdit, QVBoxLayout)


class MenuBar(QMainWindow):

    # QMainWindow has the menu bar widget
    def __init__(self):
        super().__init__()

        # create Menu Bar
        bar = self.menuBar()

        # create Root Menu
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # create actions for menu
        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+s')

        newAction = QAction('New', self)
        newAction.setShortcut('Ctrl+n')

        quitAction = QAction('Quit', self)
        quitAction.setShortcut('Ctrl+q')

        findAction = QAction('Find...', self)
        replaceAction = QAction('Replace...', self)

        # add actions to menu
        file.addAction(newAction)
        file.addAction(saveAction)
        file.addAction(quitAction)

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
        print(q.text() + ' selected')


app = QApplication(sys.argv)
menus = MenuBar()
sys.exit(app.exec_())
