# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/browser_import_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BrowserPasswordImportWindow(object):
    def setupUi(self, BrowserPasswordImportWindow):
        BrowserPasswordImportWindow.setObjectName("BrowserPasswordImportWindow")
        BrowserPasswordImportWindow.resize(1044, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BrowserPasswordImportWindow.sizePolicy().hasHeightForWidth())
        BrowserPasswordImportWindow.setSizePolicy(sizePolicy)
        BrowserPasswordImportWindow.setMinimumSize(QtCore.QSize(0, 200))
        BrowserPasswordImportWindow.setMaximumSize(QtCore.QSize(16777215, 850))
        BrowserPasswordImportWindow.setAcceptDrops(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(BrowserPasswordImportWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chk_select_all = QtWidgets.QCheckBox(BrowserPasswordImportWindow)
        self.chk_select_all.setObjectName("chk_select_all")
        self.horizontalLayout.addWidget(self.chk_select_all)
        self.label = QtWidgets.QLabel(BrowserPasswordImportWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btn_import = QtWidgets.QPushButton(BrowserPasswordImportWindow)
        self.btn_import.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_import.setObjectName("btn_import")
        self.horizontalLayout.addWidget(self.btn_import)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tbl_accounts = QtWidgets.QTableWidget(BrowserPasswordImportWindow)
        self.tbl_accounts.setObjectName("tbl_accounts")
        self.tbl_accounts.setColumnCount(0)
        self.tbl_accounts.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_accounts)

        self.retranslateUi(BrowserPasswordImportWindow)
        QtCore.QMetaObject.connectSlotsByName(BrowserPasswordImportWindow)

    def retranslateUi(self, BrowserPasswordImportWindow):
        _translate = QtCore.QCoreApplication.translate
        BrowserPasswordImportWindow.setWindowTitle(_translate("BrowserPasswordImportWindow", "Import Passwords From Browser"))
        self.chk_select_all.setText(_translate("BrowserPasswordImportWindow", "Select All"))
        self.label.setText(_translate("BrowserPasswordImportWindow", "The more accounts there are the longer it might take for the import to finish."))
        self.btn_import.setText(_translate("BrowserPasswordImportWindow", "Import"))
