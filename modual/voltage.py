#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class VoltageClass():
    '''
    电压相关操作
    '''
    def __init__(self, ui):
        self.ui = ui
        self.button_list = [self.ui.v18_Button,\
                            self.ui.v22_Button,\
                            self.ui.v26_Button,\
                            self.ui.v30_Button,\
                            self.ui.v34_Button]
        self.ui.v18_Button.clicked.connect(self.change_color)
        self.ui.v22_Button.clicked.connect(self.change_color)
        self.ui.v26_Button.clicked.connect(self.change_color)
        self.ui.v30_Button.clicked.connect(self.change_color)
        self.ui.v34_Button.clicked.connect(self.change_color)

    def change_color(self):
        self.state_list = [self.ui.v18_Button.isChecked(),\
                     self.ui.v22_Button.isChecked(),\
                     self.ui.v26_Button.isChecked(),\
                     self.ui.v30_Button.isChecked(),\
                     self.ui.v34_Button.isChecked()]
        for i in range (5):
            if self.state_list[i]:
                self.button_list[i].setStyleSheet("background-color: red")
                self.button_list[i].setChecked(False)
            else:
                self.button_list[i].setStyleSheet("")

    def reset_color(self):
        for i in range (5):
            self.button_list[i].setStyleSheet("")

    def change_grey_open(self):
        # voltage button
        self.ui.v18_Button.setEnabled(True)
        self.ui.v22_Button.setEnabled(True)
        self.ui.v26_Button.setEnabled(True)
        self.ui.v30_Button.setEnabled(True)
        self.ui.v34_Button.setEnabled(True)
        self.ui.voltage_write_Button.setEnabled(True)
        # charge button
        self.ui.r_Button.setEnabled(False)
        self.ui.ry_Button.setEnabled(False)
        self.ui.yg_Button.setEnabled(False)
        self.ui.g_Button.setEnabled(False)
        self.ui.charge_write_Button.setEnabled(False)
        # current button
        self.ui.argu_Button.setEnabled(False)
        self.ui.current_write_Button.setEnabled(False)
        # lift/right button
        self.ui.lift_Button.setEnabled(True)
        self.ui.right_Button.setEnabled(True)