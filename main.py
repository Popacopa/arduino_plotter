import typing
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from sys import argv, exit
import plotWindow
import port


res = {}
class MainWindow(QMainWindow, plotWindow.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.openPort)
        self.ports = {port.portName(): port.description() for port in QSerialPortInfo.availablePorts()}
        self.ports = list(filter(self.__func, self.ports))
        self.comboBox.addItems(self.ports)
        self.checkBox.clicked.connect(self.check)
        #self.on = self.to_bytes(41)
        #self.off = self.to_bytes(40)
    def to_bytes(self, n):...
    def check(self):
        match self.checkBox.checkState():
            case 2:serial.write(bytes([4, 1])); print(bytes([4, 1]))
            case 0:serial.write(bytes([4, 0])); print(bytes([4, 0]))

            
    def __func(self, description):
        return True if 'USB' in self.ports[description] else False
    def openPort(self):
        global view 
        global serial
        serial = QSerialPort()
        serial.BaudRate(9600)
        serial.setPortName(self.comboBox.currentText())
        serial.open(QIODevice.ReadWrite)
        #view = GraphView('port1')
        #view.show()
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