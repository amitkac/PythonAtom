# All user interface object inherit the QWidget class
# we can modify those built in features by inheriting QWidget class


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QMessageBox

# app = QApplication([])
# label = QLabel("hello bitchu")
# label.show()
# app.exec_()

app = QApplication(sys.argv)
app.setStyle('Macintosh')
window = QWidget()
layout = QVBoxLayout()
app.setStyleSheet("QPushButton { margin: 5ex; }")
button = QPushButton('Top')


def on_top_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the stupid top button!')
    alert.exec_()


button2 = QPushButton('Bottom')


def on_bottom_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the stupid bottom button!')
    alert.exec_()


window.setLayout(layout)
button2.clicked.connect(on_bottom_clicked)
button.clicked.connect(on_top_clicked)
button.show()
# window.show()
app.exec_()
