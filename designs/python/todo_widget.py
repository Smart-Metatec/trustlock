# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/todo_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_todo_tab(object):
    def setupUi(self, todo_tab):
        todo_tab.setObjectName("todo_tab")
        todo_tab.resize(573, 332)
        todo_tab.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(todo_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.form_todos = QtWidgets.QFormLayout()
        self.form_todos.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.form_todos.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.form_todos.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.form_todos.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.form_todos.setObjectName("form_todos")
        self.lne_add_todo = QtWidgets.QLineEdit(todo_tab)
        self.lne_add_todo.setMinimumSize(QtCore.QSize(300, 0))
        self.lne_add_todo.setObjectName("lne_add_todo")
        self.form_todos.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lne_add_todo)
        self.btn_add_todo = QtWidgets.QPushButton(todo_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_todo.sizePolicy().hasHeightForWidth())
        self.btn_add_todo.setSizePolicy(sizePolicy)
        self.btn_add_todo.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_add_todo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_add_todo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_todo.setObjectName("btn_add_todo")
        self.form_todos.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_add_todo)
        self.lbl_date_display = QtWidgets.QLabel(todo_tab)
        self.lbl_date_display.setObjectName("lbl_date_display")
        self.form_todos.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_date_display)
        self.dte_date_select = QtWidgets.QDateEdit(todo_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dte_date_select.sizePolicy().hasHeightForWidth())
        self.dte_date_select.setSizePolicy(sizePolicy)
        self.dte_date_select.setMinimumSize(QtCore.QSize(150, 0))
        self.dte_date_select.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dte_date_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dte_date_select.setWrapping(False)
        self.dte_date_select.setAlignment(QtCore.Qt.AlignCenter)
        self.dte_date_select.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dte_date_select.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dte_date_select.setProperty("showGroupSeparator", False)
        self.dte_date_select.setCalendarPopup(True)
        self.dte_date_select.setObjectName("dte_date_select")
        self.form_todos.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dte_date_select)
        self.verticalLayout_2.addLayout(self.form_todos)
        self.vbox_todo_container = QtWidgets.QVBoxLayout()
        self.vbox_todo_container.setObjectName("vbox_todo_container")
        self.verticalLayout_2.addLayout(self.vbox_todo_container)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(todo_tab)
        QtCore.QMetaObject.connectSlotsByName(todo_tab)

    def retranslateUi(self, todo_tab):
        _translate = QtCore.QCoreApplication.translate
        todo_tab.setWindowTitle(_translate("todo_tab", "Form"))
        self.btn_add_todo.setText(_translate("todo_tab", "Add To-do"))
        self.lbl_date_display.setText(_translate("todo_tab", "Not Set"))
