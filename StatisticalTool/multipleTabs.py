import sys
from PyQt5.QtWidgets import (QTabWidget, QWidget, QApplication, QGridLayout,
                             QLabel, QPlainTextEdit)
# from PyQt5.QtCore import Qt
# from PyQt5.QtCore import QObject


class Project(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        self.text.backgroundVisible()
        data = open('start').read()
        self.text.setPlainText(data)
        # label1 = Qlabel1()
        label2 = QLabel("Widget in Tab 2.")
        tabwidget = QTabWidget()
        tabwidget.addTab(self.text, "Start")
        tabwidget.addTab(label2, "Fitting Subplots")
        layout.addWidget(tabwidget, 0, 0)
        self.setGeometry(1024, 800, 800, 600)
        self.setWindowTitle('StatModel')
        self.initUi()

    def initUi(self):


app = QApplication(sys.argv)
screen = Project()
screen.show()
sys.exit(app.exec_())
