# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/twofa_verify_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TwofaDialog(object):
    def setupUi(self, TwofaDialog):
        TwofaDialog.setObjectName("TwofaDialog")
        TwofaDialog.resize(400, 86)
        self.verticalLayout = QtWidgets.QVBoxLayout(TwofaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_message = QtWidgets.QLabel(TwofaDialog)
        self.lbl_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_message.setObjectName("lbl_message")
        self.verticalLayout.addWidget(self.lbl_message)
        self.lnedt_code = QtWidgets.QLineEdit(TwofaDialog)
        self.lnedt_code.setObjectName("lnedt_code")
        self.verticalLayout.addWidget(self.lnedt_code)
        self.btn_verify = QtWidgets.QPushButton(TwofaDialog)
        self.btn_verify.setObjectName("btn_verify")
        self.verticalLayout.addWidget(self.btn_verify)

        self.retranslateUi(TwofaDialog)
        QtCore.QMetaObject.connectSlotsByName(TwofaDialog)

    def retranslateUi(self, TwofaDialog):
        _translate = QtCore.QCoreApplication.translate
        TwofaDialog.setWindowTitle(_translate("TwofaDialog", "Enter Two Factor Authentication Code"))
        self.lbl_message.setText(_translate("TwofaDialog", "Enter the Auth Code From Your Authenticator App"))
        self.btn_verify.setText(_translate("TwofaDialog", "Verify"))
