# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/general_vault_view_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GeneralVaultView(object):
    def setupUi(self, GeneralVaultView):
        GeneralVaultView.setObjectName("GeneralVaultView")
        GeneralVaultView.resize(621, 45)
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneralVaultView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_description = QtWidgets.QLabel(GeneralVaultView)
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.verticalLayout.addWidget(self.lbl_description)
        self.vbox_secrets = QtWidgets.QVBoxLayout()
        self.vbox_secrets.setObjectName("vbox_secrets")
        self.verticalLayout.addLayout(self.vbox_secrets)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(GeneralVaultView)
        QtCore.QMetaObject.connectSlotsByName(GeneralVaultView)

    def retranslateUi(self, GeneralVaultView):
        _translate = QtCore.QCoreApplication.translate
        GeneralVaultView.setWindowTitle(_translate("GeneralVaultView", "View Vault"))
        self.lbl_description.setText(_translate("GeneralVaultView", "TextLabel"))