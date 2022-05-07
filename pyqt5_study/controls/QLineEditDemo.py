"""
用掩码限制QLineEdit控件的输入

A   ASCII字母字符是必须输入的(A-Z、a-z)
a   ASCII字母字符是允许输入的，但不是必须的(A-Z、a-z)
N   ASCII字母字符是必须输入的(A-Z、a-z、0-9)
n   ASCII字母字符是允许输入的，但不是必须的(A-Z、a-z、0-9)
X   任何字符都是必须输入的
x   任何字符都是允许输入的，但不是必须的
9   ASCII数字字符是必须输入的(0-9)
0   ASCII数字字符是允许输入的，但不是必须的(0-9)
D   ASCII数字字符是必须输入的(1-9)
d   ASCII数字字符是允许输入的，但不是必须的(1-9)
#   ASCII数字字符或加减符号是允许输入的，但不是必须的
H   十六进制格式字符是必须输入的(A-F、a-f、1-9)
d   十六进制格式字符是允许输入的，但不是必须的(A-F、a-f、1-9)
B   二进制格式字符是必须输入的(0-1)
b   二进制格式字符是允许输入的，但不是必须的(0-1)
>   所有的字母字符都大写
<   所有的字母字符都小写
!   关闭大小写转换
\   使用"\"转义上面列出的字符
"""


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys


class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        edit1 = QLineEdit()
        # 使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4) # 不超过9999
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial', 20))

        edit2 = QLineEdit()
        # 使用float校验器
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        edit3 = QLineEdit()
        edit3.setInputMask('99-9999-999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6 = QLineEdit()
        edit6.setReadOnly(True)

        self.setWindowTitle("QLineEdit综合")
        formLayout = QFormLayout()
        formLayout.addRow('整数校验', edit1)
        formLayout.addRow('浮点数校验', edit2)
        formLayout.addRow('Input Mask', edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('密码', edit5)
        formLayout.addRow('只读', edit6)
        self.setLayout(formLayout)

    def textChanged(self, text):
        print('输入的内容：'+text)

    def enterPress(self):
        print('已输入')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QLineEditDemo()
    main.show()

    sys.exit(app.exec_())