#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
电流相关操作
    端口开关影响的按钮颜色\状态的改变
'''

class CurrentClass():
    def __init__(self, ui):
        self.ui = ui
    
    def change_grey_open(self):
        # voltage button
        self.ui.v18_Button.setEnabled(False)
        self.ui.v22_Button.setEnabled(False)
        self.ui.v26_Button.setEnabled(False)
        self.ui.v30_Button.setEnabled(False)
        self.ui.v34_Button.setEnabled(False)
        self.ui.voltage_write_Button.setEnabled(False)
        # charge button 
        self.ui.r_Button.setEnabled(False)
        self.ui.ry_Button.setEnabled(False)
        self.ui.yg_Button.setEnabled(False)
        self.ui.g_Button.setEnabled(False)
        self.ui.charge_write_Button.setEnabled(False)
        # current button
        self.ui.argu_Button.setEnabled(True)
        self.ui.current_write_Button.setEnabled(True)
        # lift/right button
        self.ui.lift_Button.setEnabled(True)
        self.ui.right_Button.setEnabled(True)
