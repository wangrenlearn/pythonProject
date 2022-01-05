import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

'''
窗口的setWindowIcon方法用于设置窗口的图标，只在Windows中可用
QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序的图标，但调用了setWindowIcon方法
QApplication中的setWindowIcon方法就只能用于应用程序图标了
'''


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口的尺寸
        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./icon.ico'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())
