import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


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

    main = IconForm()
    main.show()

    sys.exit(app.exec_())
