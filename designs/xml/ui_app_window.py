# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SA Trust PC Big\Desktop\WorkMate 3.0 Pro\designs\xml\app_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App_Window(object):
    def setupUi(self, App_Window):
        App_Window.setObjectName("App_Window")
        App_Window.resize(514, 127)
        self.verticalLayout = QtWidgets.QVBoxLayout(App_Window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.lbl_name = QtWidgets.QLabel(App_Window)
        self.lbl_name.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        self.lbl_name.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_name.setObjectName("lbl_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.lbl_group = QtWidgets.QLabel(App_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_group.sizePolicy().hasHeightForWidth())
        self.lbl_group.setSizePolicy(sizePolicy)
        self.lbl_group.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_group.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbl_group.setObjectName("lbl_group")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_group)
        self.lbl_path = QtWidgets.QLabel(App_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_path.sizePolicy().hasHeightForWidth())
        self.lbl_path.setSizePolicy(sizePolicy)
        self.lbl_path.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_path.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbl_path.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_path.setObjectName("lbl_path")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_path)
        self.lnedt_name = QtWidgets.QLineEdit(App_Window)
        self.lnedt_name.setObjectName("lnedt_name")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lnedt_name)
        self.cmb_group = QtWidgets.QComboBox(App_Window)
        self.cmb_group.setObjectName("cmb_group")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmb_group)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lnedt_path = QtWidgets.QLineEdit(App_Window)
        self.lnedt_path.setObjectName("lnedt_path")
        self.horizontalLayout.addWidget(self.lnedt_path)
        self.tbtn_desktop = QtWidgets.QToolButton(App_Window)
        self.tbtn_desktop.setText("")
        self.tbtn_desktop.setObjectName("tbtn_desktop")
        self.horizontalLayout.addWidget(self.tbtn_desktop)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.hbox_save = QtWidgets.QHBoxLayout()
        self.hbox_save.setObjectName("hbox_save")
        self.btn_save = QtWidgets.QPushButton(App_Window)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setObjectName("btn_save")
        self.hbox_save.addWidget(self.btn_save)
        self.btn_discard = QtWidgets.QPushButton(App_Window)
        self.btn_discard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_discard.setObjectName("btn_discard")
        self.hbox_save.addWidget(self.btn_discard)
        self.verticalLayout.addLayout(self.hbox_save)

        self.retranslateUi(App_Window)
        QtCore.QMetaObject.connectSlotsByName(App_Window)

    def retranslateUi(self, App_Window):
        _translate = QtCore.QCoreApplication.translate
        App_Window.setWindowTitle(_translate("App_Window", "Dialog"))
        self.lbl_name.setText(_translate("App_Window", "Name"))
        self.lbl_group.setText(_translate("App_Window", "Group"))
        self.lbl_path.setText(_translate("App_Window", "URL/Path"))
        self.btn_save.setText(_translate("App_Window", "Save"))
        self.btn_discard.setText(_translate("App_Window", "Discard"))
