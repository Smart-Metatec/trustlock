# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/forgot_question.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnswerQuestionDialog(object):
    def setupUi(self, AnswerQuestionDialog):
        AnswerQuestionDialog.setObjectName("AnswerQuestionDialog")
        AnswerQuestionDialog.resize(400, 157)
        self.verticalLayout = QtWidgets.QVBoxLayout(AnswerQuestionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_question = QtWidgets.QLabel(AnswerQuestionDialog)
        self.lbl_question.setText("")
        self.lbl_question.setObjectName("lbl_question")
        self.verticalLayout.addWidget(self.lbl_question)
        self.lnedt_answer = QtWidgets.QLineEdit(AnswerQuestionDialog)
        self.lnedt_answer.setObjectName("lnedt_answer")
        self.verticalLayout.addWidget(self.lnedt_answer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_enter = QtWidgets.QPushButton(AnswerQuestionDialog)
        self.btn_enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enter.setObjectName("btn_enter")
        self.horizontalLayout.addWidget(self.btn_enter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AnswerQuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(AnswerQuestionDialog)

    def retranslateUi(self, AnswerQuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        AnswerQuestionDialog.setWindowTitle(_translate("AnswerQuestionDialog", "Answer the question below"))
        self.btn_enter.setText(_translate("AnswerQuestionDialog", "Enter"))
