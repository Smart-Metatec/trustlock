# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/group_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupWindow(object):
    def setupUi(self, GroupWindow):
        GroupWindow.setObjectName("GroupWindow")
        GroupWindow.resize(400, 280)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(GroupWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_name = QtWidgets.QLabel(GroupWindow)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout.addWidget(self.lbl_name)
        self.lne_name = QtWidgets.QLineEdit(GroupWindow)
        self.lne_name.setObjectName("lne_name")
        self.verticalLayout.addWidget(self.lne_name)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_description = QtWidgets.QLabel(GroupWindow)
        self.lbl_description.setObjectName("lbl_description")
        self.verticalLayout_2.addWidget(self.lbl_description)
        self.lne_description = QtWidgets.QTextEdit(GroupWindow)
        self.lne_description.setObjectName("lne_description")
        self.verticalLayout_2.addWidget(self.lne_description)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(GroupWindow)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_discard = QtWidgets.QPushButton(GroupWindow)
        self.btn_discard.setObjectName("btn_discard")
        self.horizontalLayout.addWidget(self.btn_discard)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(GroupWindow)
        QtCore.QMetaObject.connectSlotsByName(GroupWindow)

    def retranslateUi(self, GroupWindow):
        _translate = QtCore.QCoreApplication.translate
        GroupWindow.setWindowTitle(_translate("GroupWindow", "Group"))
        self.lbl_name.setText(_translate("GroupWindow", "Group Name"))
        self.lbl_description.setText(_translate("GroupWindow", "Description"))
        self.btn_save.setText(_translate("GroupWindow", "Save"))
        self.btn_discard.setText(_translate("GroupWindow", "Discard"))
