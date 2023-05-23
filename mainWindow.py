import pandas as pd
from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QPushButton

from pushButton import PushButton
from tableModel import TableModel


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        self.lineEdit = QtWidgets.QLineEdit()

        self.data = [
            ["Medhat", 1101, 21],
            ["Sallam", 1102, 20],
            ["Mo Salah", 1103, 27],
            ["Yousuf", 1104, 23],
            ["Ziad", 1105, 22.1],
        ]

        self.model = TableModel(self.data)
        self.table.setModel(self.model)

        self.buttonsLayout = QHBoxLayout()
        self.insertButton = QPushButton("Insert Data")
        self.insertButton.clicked.connect(self.fetchAndClear)
        self.deleteButton = PushButton("Delete Data")
        self.executeButton = PushButton("Execute Command")
        self.buttonsLayout.addWidget(self.insertButton)
        # self.buttonsLayout.addWidget(self.deleteButton)
        # self.buttonsLayout.addWidget(self.executeButton)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.lineEdit)
        w = QWidget()
        w.setLayout(self.buttonsLayout)
        self.layout.addWidget(w)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def parseInput(self, s: str) -> list[any]:
        return list(map(lambda x: int(x) if x.isdecimal() else x,
                        s
                        .replace(" ", "")
                        .replace("[", "")
                        .replace("]", '')
                        .split(',')))

    def fetchAndClear(self):
        self.data.append(self.parseInput(self.lineEdit.text()))
        self.lineEdit.setText('')
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
