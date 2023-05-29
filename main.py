import typing
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from sys import argv, exit
import plotWindow
import port

coordX = []
coordY = []

def tryToOpen(func):
    def wrapper(self):
        if self.pushButton_2.isEnabled() == False:
            func(self)
        else:
            msg = QMessageBox()
            msg.setText('Порт не запущен!')
            msg.setWindowTitle('port_error')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
    return wrapper

class MainWindow(QMainWindow, plotWindow.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.startSerialPort)
        self.ports = {port.portName(): port.description() for port in QSerialPortInfo.availablePorts()}
        def __isUSB(description):
            return True if 'USB' in self.ports[description] else False
        self.ports = list(filter(__isUSB, self.ports))
        self.comboBox.addItems(self.ports)
        self.checkBox.clicked.connect(self.check)
        self.checkBox_2.clicked.connect(self.__check_2)
        self.checkBox_3.clicked.connect(self.__check_3)
        self.checkBox_4.clicked.connect(self.__check_4)
        self.pushButton.setEnabled(False)
    def write(self, *args):
        serial.write(bytes(*args))
    def __printData(self):
        key, x, y =  str(serial.readLine(), 'utf-8').split(';')
        if key == '1':
            coordX.append(int(x))
            coordY.append(int(y))
            view.write()
    @tryToOpen
    def check(self):
            match self.checkBox.checkState():
                case 2:serial.write(bytes([4, 1])); #print(bytes([4, 1]))
                case 0:serial.write(bytes([4, 0])); #print(bytes([4, 0]))
    @tryToOpen
    def __check_2(self):
        match self.checkBox_2.checkState():
            case 2:serial.write(bytes([5, 1])); #print(bytes([4, 1]))
            case 0:serial.write(bytes([5, 0]));
    @tryToOpen
    def __check_3(self):
         match self.checkBox_3.checkState():
            case 2:serial.write(bytes([6, 1])); #print(bytes([4, 1]))
            case 0:serial.write(bytes([6, 0]));
    @tryToOpen
    def __check_4(self):
         match self.checkBox_4.checkState():
            case 2:serial.write(bytes([7, 1])); #print(bytes([4, 1]))
            case 0:serial.write(bytes([7, 0]));
    def stopSerialPort(self):
        self.pushButton_2.setEnabled(True)
        serial.close()
        self.pushButton.setEnabled(False)
        view.close()
    def startSerialPort(self):
        global view 
        global serial
        serial = QSerialPort()
        serial.BaudRate(9600)
        serial.setPortName(self.comboBox.currentText())
        serial.open(QIODevice.ReadWrite)
        serial.readyRead.connect(self.__printData)
        self.pushButton.setEnabled(True)
        self.pushButton.clicked.connect(self.stopSerialPort)
        self.pushButton_2.setEnabled(False)
        view = GraphView('port1')
        view.show()
        if self.radioButton.isChecked():
            self.write([8, 0])
        elif self.radioButton_2.isChecked():
            self.write([9, 0])
        else:
            msg = QMessageBox()
            msg.setText('Пин не выбран!')
            msg.setWindowTitle('port_error')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            self.stopSerialPort()
""" class Message(QMessageBox):
    def __init__(self, title='none', text='unknown error'):
        self.setWindowTitle(title)
        self.setText(text)
        self.exec_() """
class GraphView(QMainWindow, port.Ui_MainWindow):
    def __init__(self, name) -> None:
        super().__init__()
        self.setWindowTitle(name)
        self.setupUi(self)
    def write(self):
        self.graph.clear()
        self.graph.plot(coordX, coordY)
def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())
if __name__ == '__main__':
    main()