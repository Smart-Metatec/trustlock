# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/app_vault_view_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AppVaultViewDialog(object):
    def setupUi(self, AppVaultViewDialog):
        AppVaultViewDialog.setObjectName("AppVaultViewDialog")
        AppVaultViewDialog.resize(617, 364)
        self.verticalLayout = QtWidgets.QVBoxLayout(AppVaultViewDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(AppVaultViewDialog)
        self.label.setMinimumSize(QtCore.QSize(125, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lbl_name = QtWidgets.QLabel(AppVaultViewDialog)
        self.lbl_name.setObjectName("lbl_name")
        self.horizontalLayout.addWidget(self.lbl_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tbtn_name = QtWidgets.QToolButton(AppVaultViewDialog)
        self.tbtn_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbtn_name.setText("")
        self.tbtn_name.setObjectName("tbtn_name")
        self.horizontalLayout.addWidget(self.tbtn_name)
        self.chk_name = QtWidgets.QCheckBox(AppVaultViewDialog)
        self.chk_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_name.setText("")
        self.chk_name.setObjectName("chk_name")
        self.horizontalLayout.addWidget(self.chk_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(AppVaultViewDialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 1))
        self.frame.setStyleSheet("background: #9ecd16;")
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(AppVaultViewDialog)
        self.label_2.setMinimumSize(QtCore.QSize(125, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lbl_username = QtWidgets.QLabel(AppVaultViewDialog)
        self.lbl_username.setObjectName("lbl_username")
        self.horizontalLayout_2.addWidget(self.lbl_username)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.tbtn_username = QtWidgets.QToolButton(AppVaultViewDialog)
        self.tbtn_username.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbtn_username.setText("")
        self.tbtn_username.setObjectName("tbtn_username")
        self.horizontalLayout_2.addWidget(self.tbtn_username)
        self.chk_username = QtWidgets.QCheckBox(AppVaultViewDialog)
        self.chk_username.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_username.setText("")
        self.chk_username.setObjectName("chk_username")
        self.horizontalLayout_2.addWidget(self.chk_username)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame_2 = QtWidgets.QFrame(AppVaultViewDialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 1))
        self.frame_2.setStyleSheet("background: #9ecd16;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(AppVaultViewDialog)
        self.label_3.setMinimumSize(QtCore.QSize(125, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lbl_email = QtWidgets.QLabel(AppVaultViewDialog)
        self.lbl_email.setObjectName("lbl_email")
        self.horizontalLayout_3.addWidget(self.lbl_email)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.tbtn_email = QtWidgets.QToolButton(AppVaultViewDialog)
        self.tbtn_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbtn_email.setText("")
        self.tbtn_email.setObjectName("tbtn_email")
        self.horizontalLayout_3.addWidget(self.tbtn_email)
        self.chk_email = QtWidgets.QCheckBox(AppVaultViewDialog)
        self.chk_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_email.setText("")
        self.chk_email.setObjectName("chk_email")
        self.horizontalLayout_3.addWidget(self.chk_email)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.frame_3 = QtWidgets.QFrame(AppVaultViewDialog)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 1))
        self.frame_3.setStyleSheet("background: #9ecd16;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(AppVaultViewDialog)
        self.label_4.setMinimumSize(QtCore.QSize(125, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lbl_password = QtWidgets.QLabel(AppVaultViewDialog)
        self.lbl_password.setObjectName("lbl_password")
        self.horizontalLayout_4.addWidget(self.lbl_password)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.tbtn_password = QtWidgets.QToolButton(AppVaultViewDialog)
        self.tbtn_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbtn_password.setText("")
        self.tbtn_password.setObjectName("tbtn_password")
        self.horizontalLayout_4.addWidget(self.tbtn_password)
        self.chk_password = QtWidgets.QCheckBox(AppVaultViewDialog)
        self.chk_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_password.setText("")
        self.chk_password.setObjectName("chk_password")
        self.horizontalLayout_4.addWidget(self.chk_password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame_4 = QtWidgets.QFrame(AppVaultViewDialog)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 1))
        self.frame_4.setStyleSheet("background: #9ecd16;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(AppVaultViewDialog)
        self.label_5.setMinimumSize(QtCore.QSize(125, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lbl_path = QtWidgets.QLabel(AppVaultViewDialog)
        self.lbl_path.setObjectName("lbl_path")
        self.horizontalLayout_5.addWidget(self.lbl_path)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.tbtn_path = QtWidgets.QToolButton(AppVaultViewDialog)
        self.tbtn_path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbtn_path.setText("")
        self.tbtn_path.setObjectName("tbtn_path")
        self.horizontalLayout_5.addWidget(self.tbtn_path)
        self.chk_path = QtWidgets.QCheckBox(AppVaultViewDialog)
        self.chk_path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_path.setText("")
        self.chk_path.setObjectName("chk_path")
        self.horizontalLayout_5.addWidget(self.chk_path)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.frame_5 = QtWidgets.QFrame(AppVaultViewDialog)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 1))
        self.frame_5.setStyleSheet("background: #9ecd16;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_open = QtWidgets.QPushButton(AppVaultViewDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_6.addWidget(self.btn_open)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(AppVaultViewDialog)
        QtCore.QMetaObject.connectSlotsByName(AppVaultViewDialog)

    def retranslateUi(self, AppVaultViewDialog):
        _translate = QtCore.QCoreApplication.translate
        AppVaultViewDialog.setWindowTitle(_translate("AppVaultViewDialog", "Your Secret App"))
        self.label.setText(_translate("AppVaultViewDialog", "App Name:"))
        self.lbl_name.setText(_translate("AppVaultViewDialog", "TextLabel"))
        self.label_2.setText(_translate("AppVaultViewDialog", "Username:"))
        self.lbl_username.setText(_translate("AppVaultViewDialog", "TextLabel"))
        self.label_3.setText(_translate("AppVaultViewDialog", "Email:"))
        self.lbl_email.setText(_translate("AppVaultViewDialog", "TextLabel"))
        self.label_4.setText(_translate("AppVaultViewDialog", "Password:"))
        self.lbl_password.setText(_translate("AppVaultViewDialog", "TextLabel"))
        self.label_5.setText(_translate("AppVaultViewDialog", "Path/URL:"))
        self.lbl_path.setText(_translate("AppVaultViewDialog", "TextLabel"))
        self.btn_open.setText(_translate("AppVaultViewDialog", "Open"))