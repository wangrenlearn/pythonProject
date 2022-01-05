# 显示控件提示消息
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget, QToolTip
from PyQt5.QtGui import QFont


class TooltipForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif',12))
        self.setToolTip('今天是<b>星期三<b>')
        self.setGeometry(300,300,400,200)
        self.setWindowTitle('设置控件提示消息')

        # 添加Button
        self.button1 = QPushButton('我是按钮')
        self.button1.setToolTip('这是一个按钮，Are you OK?')
        print(dir(self))
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        self.setLayout(layout)
        # self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())