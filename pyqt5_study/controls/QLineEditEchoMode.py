"""
QLineEdit控件与回显模式
基本功能：输入单行的文本
EchoMode(回显模式)
4种回显模式
1.Normal
2.NoEcho
3.Password
4.PasswordEcho
"""


import sys
from PyQt5.QtWidgets import *


class QlineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("passwordLineEdit", passwordLineEdit)
        formLayout.addRow("passwordEchoOnEdit", passwordEchoOnEdit)

        # placeholdertext

        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QlineEditEchoMode()
    main.show()

    sys.exit(app.exec_())