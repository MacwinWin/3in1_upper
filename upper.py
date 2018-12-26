#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
三合一仪表上位机功能:
    电压
    荷电
    电流
'''

import traceback
import sys
import serial
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
import time

from modual import ui, port, voltage, charge, current

class MyFrom(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_Button.clicked.connect(self.setup_port)
        self.ui.close_Button.clicked.connect(self.setup_port)
        self.ui.voltage_radioButton.toggled.connect(self.setup_voltage)
        self.ui.charge_radioButton.toggled.connect(self.setup_charge)
        self.ui.current_radioButton.toggled.connect(self.setup_current)
    
    def setup_port(self):
        self.port = port.PortClass(self.ui)
        if self.ui.open_Button.isEnabled():
            self.ser = self.port.init_port()
        else:
            self.ser.close()
            self.port.change_grey_close()
            self.reset_all_color()

    def setup_voltage(self):
        self.voltage = voltage.VoltageClass(self.ui)
        if self.ui.voltage_radioButton.isChecked():
            self.message = bytes().fromhex('01')
            self.ser.write(self.message)
            time.sleep(0.1)
            print(self.ser.read_all())
        else:
            pass
        if self.ui.voltage_radioButton.isChecked():
            self.voltage.change_grey_open()
        elif not self.ui.voltage_radioButton.isChecked():
            self.voltage.reset_color()

    def setup_charge(self):
        self.charge = charge.ChargeClass(self.ui)
        if self.ui.charge_radioButton.isChecked():
            self.message = bytes().fromhex('02')
            self.ser.write(self.message)
            time.sleep(0.1)
            print(self.ser.read_all())
        else:
            pass
        if self.ui.charge_radioButton.isChecked():
            self.charge.change_grey_open()
        elif not self.ui.charge_radioButton.isChecked():
            self.charge.reset_color()
    
    def setup_current(self):
        self.current = current.CurrentClass(self.ui)
        if self.ui.current_radioButton.isChecked():
            self.message = bytes().fromhex('03')
            self.ser.write(self.message)
            time.sleep(0.1)
            print(self.ser.read_all())
        else:
            pass
        if self.ui.current_radioButton.isChecked():
            self.current.change_grey_open()

    def reset_all_color(self):
        self.voltage = voltage.VoltageClass(self.ui)
        self.charge = charge.ChargeClass(self.ui)
        self.voltage.reset_color()
        self.charge.reset_color()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = MyFrom()
#    app.setWindowIcon(QIcon())
    w.show()
    sys.exit(app.exec_())
