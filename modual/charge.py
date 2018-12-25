#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
荷电相关操作
    按钮按下变红
    端口开关影响的按钮颜色\状态的改变
'''

class ChargeClass():
    def __init__(self, ui):
        self.ui = ui 
        self.button_list = [self.ui.r_Button,\
                            self.ui.ry_Button,\
                            self.ui.yg_Button,\
                            self.ui.g_Button]
        self.ui.r_Button.clicked.connect(self.change_color)
        self.ui.ry_Button.clicked.connect(self.change_color)
        self.ui.yg_Button.clicked.connect(self.change_color)
        self.ui.g_Button.clicked.connect(self.change_color)

    def change_color(self):
        self.state_list = [self.ui.r_Button.isChecked(),\
                           self.ui.ry_Button.isChecked(),\
                           self.ui.yg_Button.isChecked(),\
                           self.ui.g_Button.isChecked()]
        for i in range(4):
            if self.state_list[i]:
                self.button_list[i].setStyleSheet("background-color: red")
                self.button_list[i].setChecked(False)
            else:
                self.button_list[i].setStyleSheet("")

    def reset_color(self):
        for i in range(4):
            self.button_list[i].setStyleSheet("")
    
    def change_grey_open(self):
        # voltage button
        self.ui.v18_Button.setEnabled(False)
        self.ui.v22_Button.setEnabled(False)
        self.ui.v26_Button.setEnabled(False)
        self.ui.v30_Button.setEnabled(False)
        self.ui.v34_Button.setEnabled(False)
        self.ui.voltage_write_Button.setEnabled(False)
        # charge button 
        self.ui.r_Button.setEnabled(True)
        self.ui.ry_Button.setEnabled(True)
        self.ui.yg_Button.setEnabled(True)
        self.ui.g_Button.setEnabled(True)
        self.ui.charge_write_Button.setEnabled(True)
        # current button
        self.ui.argu_Button.setEnabled(False)
        self.ui.current_write_Button.setEnabled(False)
        # lift/right button
        self.ui.lift_Button.setEnabled(True)
        self.ui.right_Button.setEnabled(True)