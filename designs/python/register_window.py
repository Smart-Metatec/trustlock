# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(461, 291)
        self.verticalLayout = QtWidgets.QVBoxLayout(Register)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_intro = QtWidgets.QLabel(Register)
        self.lbl_intro.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_intro.setObjectName("lbl_intro")
        self.verticalLayout_2.addWidget(self.lbl_intro)
        self.lbl_company = QtWidgets.QLabel(Register)
        self.lbl_company.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_company.setObjectName("lbl_company")
        self.verticalLayout_2.addWidget(self.lbl_company)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.form_register = QtWidgets.QFormLayout()
        self.form_register.setObjectName("form_register")
        self.lbl_name = QtWidgets.QLabel(Register)
        self.lbl_name.setObjectName("lbl_name")
        self.form_register.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.lbl_password = QtWidgets.QLabel(Register)
        self.lbl_password.setObjectName("lbl_password")
        self.form_register.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        self.lbl_question = QtWidgets.QLabel(Register)
        self.lbl_question.setObjectName("lbl_question")
        self.form_register.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_question)
        self.lbl_answer = QtWidgets.QLabel(Register)
        self.lbl_answer.setObjectName("lbl_answer")
        self.form_register.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_answer)
        self.lbl_password2 = QtWidgets.QLabel(Register)
        self.lbl_password2.setObjectName("lbl_password2")
        self.form_register.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_password2)
        self.lbl_email = QtWidgets.QLabel(Register)
        self.lbl_email.setObjectName("lbl_email")
        self.form_register.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_email)
        self.lnedt_name = QtWidgets.QLineEdit(Register)
        self.lnedt_name.setObjectName("lnedt_name")
        self.form_register.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lnedt_name)
        self.lnedt_email = QtWidgets.QLineEdit(Register)
        self.lnedt_email.setObjectName("lnedt_email")
        self.form_register.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lnedt_email)
        self.lnedt_password = QtWidgets.QLineEdit(Register)
        self.lnedt_password.setObjectName("lnedt_password")
        self.form_register.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lnedt_password)
        self.lnedt_password2 = QtWidgets.QLineEdit(Register)
        self.lnedt_password2.setObjectName("lnedt_password2")
        self.form_register.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lnedt_password2)
        self.lnedt_question = QtWidgets.QLineEdit(Register)
        self.lnedt_question.setObjectName("lnedt_question")
        self.form_register.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lnedt_question)
        self.lnedt_answer = QtWidgets.QLineEdit(Register)
        self.lnedt_answer.setObjectName("lnedt_answer")
        self.form_register.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lnedt_answer)
        self.verticalLayout.addLayout(self.form_register)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_register = QtWidgets.QPushButton(Register)
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout.addWidget(self.btn_register)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.lbl_intro.setText(_translate("Register", "Proudly brought to you by"))
        self.lbl_company.setText(_translate("Register", "Smart MetaTec"))
        self.lbl_name.setText(_translate("Register", "Name"))
        self.lbl_password.setText(_translate("Register", "Password"))
        self.lbl_question.setText(_translate("Register", "Security Question"))
        self.lbl_answer.setText(_translate("Register", "Answer"))
        self.lbl_password2.setText(_translate("Register", "Confirm Password"))
        self.lbl_email.setText(_translate("Register", "Email"))
        self.btn_register.setText(_translate("Register", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
