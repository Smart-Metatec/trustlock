# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SA Trust PC Big\Desktop\WorkMate 3.0 Pro\designs\xml\timer_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Timer(object):
    def setupUi(self, Timer):
        Timer.setObjectName("Timer")
        Timer.resize(381, 240)
        self.verticalLayout = QtWidgets.QVBoxLayout(Timer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_vault_timer = QtWidgets.QLabel(Timer)
        self.lbl_vault_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_vault_timer.setObjectName("lbl_vault_timer")
        self.verticalLayout.addWidget(self.lbl_vault_timer)
        self.lcd_timer = QtWidgets.QLCDNumber(Timer)
        self.lcd_timer.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_timer.setSmallDecimalPoint(False)
        self.lcd_timer.setDigitCount(12)
        self.lcd_timer.setObjectName("lcd_timer")
        self.verticalLayout.addWidget(self.lcd_timer)
        self.hslide_timer = QtWidgets.QSlider(Timer)
        self.hslide_timer.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.hslide_timer.setMinimum(1)
        self.hslide_timer.setMaximum(60)
        self.hslide_timer.setTracking(True)
        self.hslide_timer.setOrientation(QtCore.Qt.Horizontal)
        self.hslide_timer.setInvertedAppearance(False)
        self.hslide_timer.setInvertedControls(True)
        self.hslide_timer.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.hslide_timer.setTickInterval(0)
        self.hslide_timer.setObjectName("hslide_timer")
        self.verticalLayout.addWidget(self.hslide_timer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(Timer)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Timer)
        QtCore.QMetaObject.connectSlotsByName(Timer)

    def retranslateUi(self, Timer):
        _translate = QtCore.QCoreApplication.translate
        Timer.setWindowTitle(_translate("Timer", "Timer"))
        self.lbl_vault_timer.setText(_translate("Timer", "Set the vault timer in minutes"))
        self.btn_save.setText(_translate("Timer", "Save"))
