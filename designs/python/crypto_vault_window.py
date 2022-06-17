# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/crypto_vault_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CryptoVault(object):
    def setupUi(self, CryptoVault):
        CryptoVault.setObjectName("CryptoVault")
        CryptoVault.resize(400, 407)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(CryptoVault)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbl_description = QtWidgets.QLabel(CryptoVault)
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.verticalLayout_7.addWidget(self.lbl_description)
        self.lne_description = QtWidgets.QLineEdit(CryptoVault)
        self.lne_description.setObjectName("lne_description")
        self.verticalLayout_7.addWidget(self.lne_description)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_name = QtWidgets.QLabel(CryptoVault)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout.addWidget(self.lbl_name)
        self.lne_name = QtWidgets.QLineEdit(CryptoVault)
        self.lne_name.setObjectName("lne_name")
        self.verticalLayout.addWidget(self.lne_name)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_words = QtWidgets.QLabel(CryptoVault)
        self.lbl_words.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_words.setObjectName("lbl_words")
        self.verticalLayout_2.addWidget(self.lbl_words)
        self.cmb_num_words = QtWidgets.QComboBox(CryptoVault)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_num_words.sizePolicy().hasHeightForWidth())
        self.cmb_num_words.setSizePolicy(sizePolicy)
        self.cmb_num_words.setObjectName("cmb_num_words")
        self.cmb_num_words.addItem("")
        self.cmb_num_words.addItem("")
        self.cmb_num_words.addItem("")
        self.cmb_num_words.addItem("")
        self.cmb_num_words.addItem("")
        self.verticalLayout_2.addWidget(self.cmb_num_words)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_password = QtWidgets.QLabel(CryptoVault)
        self.lbl_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_password.setObjectName("lbl_password")
        self.verticalLayout_5.addWidget(self.lbl_password)
        self.lne_password1 = QtWidgets.QLineEdit(CryptoVault)
        self.lne_password1.setObjectName("lne_password1")
        self.verticalLayout_5.addWidget(self.lne_password1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_password2 = QtWidgets.QLabel(CryptoVault)
        self.lbl_password2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_password2.setObjectName("lbl_password2")
        self.verticalLayout_6.addWidget(self.lbl_password2)
        self.lne_password2 = QtWidgets.QLineEdit(CryptoVault)
        self.lne_password2.setObjectName("lne_password2")
        self.verticalLayout_6.addWidget(self.lne_password2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.frame = QtWidgets.QFrame(CryptoVault)
        self.frame.setStyleSheet("background-color: #9ecd16;")
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_3.addWidget(self.frame)
        self.gbox_words = QtWidgets.QGridLayout()
        self.gbox_words.setContentsMargins(-1, 5, -1, -1)
        self.gbox_words.setObjectName("gbox_words")
        self.verticalLayout_3.addLayout(self.gbox_words)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_save = QtWidgets.QPushButton(CryptoVault)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CryptoVault)
        QtCore.QMetaObject.connectSlotsByName(CryptoVault)

    def retranslateUi(self, CryptoVault):
        _translate = QtCore.QCoreApplication.translate
        CryptoVault.setWindowTitle(_translate("CryptoVault", "Add Crypto Secret"))
        self.lbl_description.setText(_translate("CryptoVault", "Description"))
        self.lbl_name.setText(_translate("CryptoVault", "Username"))
        self.lbl_words.setText(_translate("CryptoVault", "Number of Words"))
        self.cmb_num_words.setItemText(0, _translate("CryptoVault", "12 Words"))
        self.cmb_num_words.setItemText(1, _translate("CryptoVault", "15 Words"))
        self.cmb_num_words.setItemText(2, _translate("CryptoVault", "18 Words"))
        self.cmb_num_words.setItemText(3, _translate("CryptoVault", "21 Words"))
        self.cmb_num_words.setItemText(4, _translate("CryptoVault", "24 Words"))
        self.lbl_password.setText(_translate("CryptoVault", "Password"))
        self.lbl_password2.setText(_translate("CryptoVault", "Confirm Password"))
        self.btn_save.setText(_translate("CryptoVault", "Save"))
