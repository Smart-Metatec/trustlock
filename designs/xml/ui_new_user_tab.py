# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SA Trust PC Big\Desktop\WorkMate 3.0 Pro\designs\xml\new_user_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_user(object):
    def setupUi(self, new_user):
        new_user.setObjectName("new_user")
        new_user.resize(730, 494)
        self.verticalLayout = QtWidgets.QVBoxLayout(new_user)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.lbl_generate_password = QtWidgets.QLabel(new_user)
        self.lbl_generate_password.setObjectName("lbl_generate_password")
        self.horizontalLayout_11.addWidget(self.lbl_generate_password)
        self.tbtn_generate_password = QtWidgets.QToolButton(new_user)
        self.tbtn_generate_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbtn_generate_password.setText("")
        self.tbtn_generate_password.setObjectName("tbtn_generate_password")
        self.horizontalLayout_11.addWidget(self.tbtn_generate_password)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl_name = QtWidgets.QLabel(new_user)
        self.lbl_name.setObjectName("lbl_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.lnedt_name = QtWidgets.QLineEdit(new_user)
        self.lnedt_name.setObjectName("lnedt_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lnedt_name)
        self.lbl_email = QtWidgets.QLabel(new_user)
        self.lbl_email.setObjectName("lbl_email")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_email)
        self.lnedt_email = QtWidgets.QLineEdit(new_user)
        self.lnedt_email.setObjectName("lnedt_email")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lnedt_email)
        self.lbl_password = QtWidgets.QLabel(new_user)
        self.lbl_password.setObjectName("lbl_password")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lnedt_password = QtWidgets.QLineEdit(new_user)
        self.lnedt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lnedt_password.setObjectName("lnedt_password")
        self.horizontalLayout_9.addWidget(self.lnedt_password)
        self.chk_password = QtWidgets.QCheckBox(new_user)
        self.chk_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_password.setText("")
        self.chk_password.setObjectName("chk_password")
        self.horizontalLayout_9.addWidget(self.chk_password)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.lbl_password2 = QtWidgets.QLabel(new_user)
        self.lbl_password2.setObjectName("lbl_password2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_password2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lnedt_password2 = QtWidgets.QLineEdit(new_user)
        self.lnedt_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lnedt_password2.setObjectName("lnedt_password2")
        self.horizontalLayout_12.addWidget(self.lnedt_password2)
        self.chk_password2 = QtWidgets.QCheckBox(new_user)
        self.chk_password2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_password2.setText("")
        self.chk_password2.setObjectName("chk_password2")
        self.horizontalLayout_12.addWidget(self.chk_password2)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.lbl_password_exp = QtWidgets.QLabel(new_user)
        self.lbl_password_exp.setObjectName("lbl_password_exp")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_password_exp)
        self.dte_password_exp = QtWidgets.QDateEdit(new_user)
        self.dte_password_exp.setCalendarPopup(True)
        self.dte_password_exp.setObjectName("dte_password_exp")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dte_password_exp)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_passphrase_desc = QtWidgets.QLabel(new_user)
        self.lbl_passphrase_desc.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lbl_passphrase_desc.setStyleSheet("")
        self.lbl_passphrase_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_passphrase_desc.setObjectName("lbl_passphrase_desc")
        self.verticalLayout_6.addWidget(self.lbl_passphrase_desc)
        self.word_widget = QtWidgets.QWidget(new_user)
        self.word_widget.setObjectName("word_widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.word_widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gbox_words = QtWidgets.QGridLayout()
        self.gbox_words.setObjectName("gbox_words")
        self.verticalLayout_8.addLayout(self.gbox_words)
        self.verticalLayout_6.addWidget(self.word_widget)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btn_copy = QtWidgets.QPushButton(new_user)
        self.btn_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy.setObjectName("btn_copy")
        self.horizontalLayout_13.addWidget(self.btn_copy)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btn_register = QtWidgets.QPushButton(new_user)
        self.btn_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout_14.addWidget(self.btn_register)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.retranslateUi(new_user)
        QtCore.QMetaObject.connectSlotsByName(new_user)

    def retranslateUi(self, new_user):
        _translate = QtCore.QCoreApplication.translate
        new_user.setWindowTitle(_translate("new_user", "Form"))
        self.lbl_generate_password.setText(_translate("new_user", "Password Generator"))
        self.lbl_name.setText(_translate("new_user", "Name*"))
        self.lbl_email.setText(_translate("new_user", "Email*"))
        self.lbl_password.setText(_translate("new_user", "Password*"))
        self.lbl_password2.setText(_translate("new_user", "Confirm Password*"))
        self.lbl_password_exp.setText(_translate("new_user", "Password Expiration"))
        self.lbl_passphrase_desc.setText(_translate("new_user", "Keys:"))
        self.btn_copy.setText(_translate("new_user", "Copy"))
        self.btn_register.setText(_translate("new_user", "Register"))
