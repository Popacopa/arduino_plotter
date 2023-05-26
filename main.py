import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from sys import argv, exit
import plotWindow
import port

class MainWindow(QMainWindow, plotWindow.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.openPort)
    def openPort(self):
        global view 
        view = GraphView('port1')
        view.show()
class GraphView(QMainWindow, port.Ui_MainWindow):
    def __init__(self, name) -> None:
        super().__init__()
        self.setWindowTitle(name)
        self.setupUi(self)

def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())
if __name__ == '__main__':
    main()