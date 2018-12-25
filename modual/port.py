#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
端口相关操作
    初始化端口
    写端口
    端口开关导致其他按钮开关
'''

import serial
import time

class PortClass():
    '''
    初始化/关闭串口
    '''
    def __init__(self, ui):
        self.ui = ui
        self.ui.v18_Button.clicked.connect(self.write_port)
        self.ui.v22_Button.clicked.connect(self.write_port)
        self.ui.v26_Button.clicked.connect(self.write_port)
        self.ui.v30_Button.clicked.connect(self.write_port)
        self.ui.v34_Button.clicked.connect(self.write_port)
        self.ui.voltage_write_Button.clicked.connect(self.write_port)
        self.ui.r_Button.clicked.connect(self.write_port)
        self.ui.ry_Button.clicked.connect(self.write_port)
        self.ui.yg_Button.clicked.connect(self.write_port)
        self.ui.g_Button.clicked.connect(self.write_port)
        self.ui.charge_write_Button.clicked.connect(self.write_port)
        self.ui.argu_Button.clicked.connect(self.write_port)
        self.ui.current_write_Button.clicked.connect(self.write_port)
        self.ui.lift_Button.clicked.connect(self.write_port)
        self.ui.right_Button.clicked.connect(self.write_port)

    def init_port(self):
        portName = self.ui.port_Box.currentText()
        try:
            self.ser = serial.Serial(portName)
            self.change_grey_open()
            print(portName)
            return self.ser
        except:
            QMessageBox.warning(None, '串口', "串口未开启", QMessageBox.Ok)
            return

    def write_port(self):
        if self.ui.v18_Button.isChecked():
            self.message = bytes().fromhex('04')
            self.ser.write(self.message)
            print('18')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.v22_Button.isChecked():
            self.message = bytes().fromhex('05')
            self.ser.write(self.message)
            print('22')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.v26_Button.isChecked():
            self.message = bytes().fromhex('06')
            self.ser.write(self.message)
            print('26')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.v30_Button.isChecked():
            self.message = bytes().fromhex('07')
            self.ser.write(self.message)
            print('30')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.v34_Button.isChecked():
            self.message = bytes().fromhex('08')
            self.ser.write(self.message)
            print('34')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.voltage_write_Button.isChecked():
            self.message = bytes().fromhex('16')
            self.ser.write(self.message)
            print('saved voltage')
            self.ui.voltage_write_Button.setChecked(False)
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.r_Button.isChecked():
            self.message = bytes().fromhex('19')
            self.ser.write(self.message)
            print('red')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.ry_Button.isChecked():
            self.message = bytes().fromhex('10')
            self.ser.write(self.message)
            print('red yellow')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.yg_Button.isChecked():
            self.message = bytes().fromhex('11')
            self.ser.write(self.message)
            print('yellow green')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.g_Button.isChecked():
            self.message = bytes().fromhex('12')
            self.ser.write(self.message)
            print('green')
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.charge_write_Button.isChecked():
            self.message = bytes().fromhex('17')
            self.ser.write(self.message)
            print('saved charge')
            self.ui.charge_write_Button.setChecked(False)
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.argu_Button.isChecked():
            self.message = bytes().fromhex('13')
            self.ser.write(self.message)
            print('current')
            self.ui.argu_Button.setChecked(False)
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.current_write_Button.isChecked():
            self.message = bytes().fromhex('18')
            self.ser.write(self.message)
            print('saved current')
            self.ui.current_write_Button.setChecked(False)
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.lift_Button.isChecked():
            self.message = bytes().fromhex('14')
            self.ser.write(self.message)
            print('lift')
            self.ui.lift_Button.setChecked(False)
            time.sleep(0.1)
            print(self.ser.read_all())
        elif self.ui.right_Button.isChecked():
            self.message = bytes().fromhex('15')
            self.ser.write(self.message)
            print('right')
            self.ui.right_Button.setChecked(False)
            time.sleep(0.1)
            print(self.ser.read_all())
        
    def change_grey_close(self):
        self.ui.open_Button.setEnabled(True)
        self.ui.port_Box.setEnabled(True)
        self.ui.close_Button.setEnabled(False)
        self.ui.voltage_radioButton.setEnabled(False)
        self.ui.voltage_radioButton.setCheckable(False)
        self.ui.charge_radioButton.setEnabled(False)
        self.ui.charge_radioButton.setCheckable(False)
        self.ui.current_radioButton.setEnabled(False)
        self.ui.current_radioButton.setCheckable(False)
        self.ui.v18_Button.setEnabled(False)
        self.ui.v22_Button.setEnabled(False)
        self.ui.v26_Button.setEnabled(False)
        self.ui.v30_Button.setEnabled(False)
        self.ui.v34_Button.setEnabled(False)
        self.ui.r_Button.setEnabled(False)
        self.ui.ry_Button.setEnabled(False)
        self.ui.yg_Button.setEnabled(False)
        self.ui.g_Button.setEnabled(False)
        self.ui.lift_Button.setEnabled(False)
        self.ui.right_Button.setEnabled(False)
        self.ui.argu_Button.setEnabled(False)
        self.ui.voltage_write_Button.setEnabled(False)
        self.ui.charge_write_Button.setEnabled(False)
        self.ui.current_write_Button.setEnabled(False)

    def change_grey_open(self):
        self.ui.open_Button.setEnabled(False)
        self.ui.port_Box.setEnabled(False)
        self.ui.close_Button.setEnabled(True)
        self.ui.voltage_radioButton.setEnabled(True)
        self.ui.voltage_radioButton.setCheckable(True)
        self.ui.charge_radioButton.setEnabled(True)
        self.ui.charge_radioButton.setCheckable(True)
        self.ui.current_radioButton.setEnabled(True)
        self.ui.current_radioButton.setCheckable(True)