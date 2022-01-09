import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
'''
窗口的setWindowIcon方法用于设置窗口的图标，只在windows中可用
QApplication中的setWindowIcon方法用于设置窗口和应用程序图标，但调用了窗口的setWindowIcon方法
QApplication中的setWindowIcon方法就只能用于应用程序图标(macos)
'''


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置主窗口的标题
        self.setWindowTitle('设置窗口图标')
        # 设置窗口的坐标尺寸
        self.setGeometry(300, 300, 400, 250)
        # 设置窗口图标
        self.setWindowIcon(QIcon('./icon.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('./icon.ico'))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())
