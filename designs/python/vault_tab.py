# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/vault_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Vault_tab(object):
    def setupUi(self, Vault_tab):
        Vault_tab.setObjectName("Vault_tab")
        Vault_tab.resize(640, 382)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Vault_tab.sizePolicy().hasHeightForWidth())
        Vault_tab.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Vault_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hbox_controls = QtWidgets.QHBoxLayout()
        self.hbox_controls.setObjectName("hbox_controls")
        self.chk_edit = QtWidgets.QCheckBox(Vault_tab)
        self.chk_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_edit.setObjectName("chk_edit")
        self.hbox_controls.addWidget(self.chk_edit)
        self.chk_delete = QtWidgets.QCheckBox(Vault_tab)
        self.chk_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_delete.setTristate(False)
        self.chk_delete.setObjectName("chk_delete")
        self.hbox_controls.addWidget(self.chk_delete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_controls.addItem(spacerItem)
        self.btn_add = QtWidgets.QPushButton(Vault_tab)
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add.setObjectName("btn_add")
        self.hbox_controls.addWidget(self.btn_add)
        self.btn_login = QtWidgets.QPushButton(Vault_tab)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setObjectName("btn_login")
        self.hbox_controls.addWidget(self.btn_login)
        self.verticalLayout.addLayout(self.hbox_controls)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.lbl_app_vault = QtWidgets.QLabel(Vault_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_app_vault.sizePolicy().hasHeightForWidth())
        self.lbl_app_vault.setSizePolicy(sizePolicy)
        self.lbl_app_vault.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_app_vault.setObjectName("lbl_app_vault")
        self.horizontalLayout_4.addWidget(self.lbl_app_vault)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.scrollArea = QtWidgets.QScrollArea(Vault_tab)
        self.scrollArea.setStyleSheet("padding: 0px;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 196, 301))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vbox_app_vault = QtWidgets.QVBoxLayout()
        self.vbox_app_vault.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vbox_app_vault.setSpacing(6)
        self.vbox_app_vault.setObjectName("vbox_app_vault")
        self.verticalLayout_5.addLayout(self.vbox_app_vault)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.frame = QtWidgets.QFrame(Vault_tab)
        self.frame.setMinimumSize(QtCore.QSize(1, 0))
        self.frame.setMaximumSize(QtCore.QSize(1, 16777215))
        self.frame.setStyleSheet("background-color: #9ecd16;width: 1px")
        self.frame.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.lbl_crypto_vault = QtWidgets.QLabel(Vault_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_crypto_vault.sizePolicy().hasHeightForWidth())
        self.lbl_crypto_vault.setSizePolicy(sizePolicy)
        self.lbl_crypto_vault.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_crypto_vault.setObjectName("lbl_crypto_vault")
        self.horizontalLayout_5.addWidget(self.lbl_crypto_vault)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.scrollArea_2 = QtWidgets.QScrollArea(Vault_tab)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 196, 301))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vbox_crypto_vault = QtWidgets.QVBoxLayout()
        self.vbox_crypto_vault.setObjectName("vbox_crypto_vault")
        self.verticalLayout_6.addLayout(self.vbox_crypto_vault)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.frame_2 = QtWidgets.QFrame(Vault_tab)
        self.frame_2.setMinimumSize(QtCore.QSize(1, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(1, 16777215))
        self.frame_2.setStyleSheet("background-color: #9ecd16;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.lbl_general_vault = QtWidgets.QLabel(Vault_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_general_vault.sizePolicy().hasHeightForWidth())
        self.lbl_general_vault.setSizePolicy(sizePolicy)
        self.lbl_general_vault.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_general_vault.setObjectName("lbl_general_vault")
        self.horizontalLayout_6.addWidget(self.lbl_general_vault)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.scrollArea_3 = QtWidgets.QScrollArea(Vault_tab)
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 196, 301))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.vbox_general_vault = QtWidgets.QVBoxLayout()
        self.vbox_general_vault.setObjectName("vbox_general_vault")
        self.verticalLayout_7.addLayout(self.vbox_general_vault)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.addWidget(self.scrollArea_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Vault_tab)
        QtCore.QMetaObject.connectSlotsByName(Vault_tab)

    def retranslateUi(self, Vault_tab):
        _translate = QtCore.QCoreApplication.translate
        Vault_tab.setWindowTitle(_translate("Vault_tab", "Form"))
        self.chk_edit.setText(_translate("Vault_tab", "Edit Secret"))
        self.chk_delete.setText(_translate("Vault_tab", "Delete Secret"))
        self.btn_add.setText(_translate("Vault_tab", "Add Secret"))
        self.btn_login.setText(_translate("Vault_tab", "Login"))
        self.lbl_app_vault.setText(_translate("Vault_tab", "App Vault"))
        self.lbl_crypto_vault.setText(_translate("Vault_tab", "Crypto Wallet"))
        self.lbl_general_vault.setText(_translate("Vault_tab", "General Vault"))
