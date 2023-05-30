import typing
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from sys import argv, exit
import plotWindow
import port

coordX = []           # X axis coordinate array
coordY = []           # Y axis coordinate array
filt = 2        

def tryToOpen(func):  # to send the port_error messange
    def wrapper(self):
        if self.pushButton_2.isEnabled() == False:
            func(self)
        else:
            msg = QMessageBox()                    # messenge
            msg.setText('Порт не запущен!')        # text of messange
            msg.setWindowTitle('port_error')       # title of messange
            msg.setIcon(QMessageBox.Warning)       # icon of messange
            msg.exec_()
    return wrapper

class MainWindow(QMainWindow, plotWindow.Ui_MainWindow):                 # the main window class 
    def __init__(self) -> None:                                          # the main window constructor
        super().__init__()
        self.setupUi(self)                                               # initing UI in Main window
        self.pushButton_2.clicked.connect(self.startSerialPort)          # listening pushing
        self.ports = {port.portName(): port.description() for port in QSerialPortInfo.availablePorts()}             #getting available ports
        def __isUSB(description):                                        # the filter function, that filter available USB ports
            return True if 'USB' in self.ports[description] else False
        self.ports = list(filter(__isUSB, self.ports))                   # filter available USB ports
        self.comboBox.addItems(self.ports)                               # add ports to combo box
        self.checkBox.clicked.connect(self.check)                        # listening pushing
        self.checkBox_2.clicked.connect(self.__check_2)                  # listening pushing
        self.checkBox_3.clicked.connect(self.__check_3)                  # listening pushing
        self.checkBox_4.clicked.connect(self.__check_4)                  # listening pushing
        self.pushButton.setEnabled(False)                                # setting status
    def write(self, *args):                                              # write to serial
        serial.write(bytes(*args))
    def __printData(self):                                               # get data from serial
        key, x, y =  str(serial.readLine(), 'utf-8').strip().split(';')
        if len(coordY) > 0:
            if abs(coordY[-1] - int(y)) <= filt:
                y = coordY[-1]
        coordX.append(int(x))
        coordY.append(int(y)) 
        if len(coordX) > 400:
            coordX.pop(0)
            coordY.pop(0) 
        view.write()                                                 # paint the graph!!!
    @tryToOpen
    def check(self):
            match self.checkBox.checkState():
                case 2:serial.write(bytes([4, 1])); 
                case 0:serial.write(bytes([4, 0])); 
    @tryToOpen
    def __check_2(self):
        match self.checkBox_2.checkState():
            case 2:serial.write(bytes([5, 1])); 
            case 0:serial.write(bytes([5, 0]));
    @tryToOpen
    def __check_3(self):
         match self.checkBox_3.checkState():
            case 2:serial.write(bytes([6, 1])); 
            case 0:serial.write(bytes([6, 0]));
    @tryToOpen
    def __check_4(self):
         match self.checkBox_4.checkState():
            case 2:serial.write(bytes([7, 1])); 
            case 0:serial.write(bytes([7, 0]));
    def stopSerialPort(self):
        serial.close()
        view.close()
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(False)
    def startSerialPort(self):
        global view 
        global serial
        serial = QSerialPort()
        serial.BaudRate(9600)
        serial.setPortName(self.comboBox.currentText())
        serial.open(QIODevice.ReadWrite)
        view = GraphView('port1')
        if self.radioButton.isChecked():
            self.write([8, 0])
            view.show()
        elif self.radioButton_2.isChecked():
            self.write([9, 0])
            view.show()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton.clicked.connect(self.stopSerialPort)
        serial.readyRead.connect(self.__printData)
class GraphView(QMainWindow, port.Ui_MainWindow):
    def __init__(self, name) -> None:
        super().__init__()
        self.setWindowTitle(name)
        self.setupUi(self)
        #self.graph.set
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