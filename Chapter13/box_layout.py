from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app1 = QApplication([])
make_window = QWidget()
layout = QVBoxLayout()

layout.addWidget(QPushButton('Button 1'))
layout.addWidget(QPushButton('Button 2'))

make_window.setLayout(layout)
make_window.show()

app1.exec()
