# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/generate_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GeneratePasswordWindow(object):
    def setupUi(self, GeneratePasswordWindow):
        GeneratePasswordWindow.setObjectName("GeneratePasswordWindow")
        GeneratePasswordWindow.resize(472, 437)
        GeneratePasswordWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        GeneratePasswordWindow.setToolTip("")
        GeneratePasswordWindow.setStatusTip("")
        GeneratePasswordWindow.setWhatsThis("")
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneratePasswordWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_password = QtWidgets.QLabel(GeneratePasswordWindow)
        self.lbl_password.setObjectName("lbl_password")
        self.horizontalLayout.addWidget(self.lbl_password)
        self.lne_password = QtWidgets.QLineEdit(GeneratePasswordWindow)
        self.lne_password.setObjectName("lne_password")
        self.horizontalLayout.addWidget(self.lne_password)
        self.chk_show = QtWidgets.QCheckBox(GeneratePasswordWindow)
        self.chk_show.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_show.setText("")
        self.chk_show.setObjectName("chk_show")
        self.horizontalLayout.addWidget(self.chk_show)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bar_strength = QtWidgets.QProgressBar(GeneratePasswordWindow)
        self.bar_strength.setMaximum(150)
        self.bar_strength.setProperty("value", 0)
        self.bar_strength.setOrientation(QtCore.Qt.Horizontal)
        self.bar_strength.setFormat("")
        self.bar_strength.setObjectName("bar_strength")
        self.verticalLayout_3.addWidget(self.bar_strength)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.frame_checkbox_container = QtWidgets.QFrame(GeneratePasswordWindow)
        self.frame_checkbox_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_checkbox_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_checkbox_container.setObjectName("frame_checkbox_container")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_checkbox_container)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chk_uppercase = QtWidgets.QCheckBox(self.frame_checkbox_container)
        self.chk_uppercase.setMinimumSize(QtCore.QSize(0, 30))
        self.chk_uppercase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_uppercase.setObjectName("chk_uppercase")
        self.verticalLayout_2.addWidget(self.chk_uppercase)
        self.chk_lowercase = QtWidgets.QCheckBox(self.frame_checkbox_container)
        self.chk_lowercase.setMinimumSize(QtCore.QSize(0, 30))
        self.chk_lowercase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_lowercase.setObjectName("chk_lowercase")
        self.verticalLayout_2.addWidget(self.chk_lowercase)
        self.chk_numbers = QtWidgets.QCheckBox(self.frame_checkbox_container)
        self.chk_numbers.setMinimumSize(QtCore.QSize(0, 30))
        self.chk_numbers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_numbers.setObjectName("chk_numbers")
        self.verticalLayout_2.addWidget(self.chk_numbers)
        self.chk_math = QtWidgets.QCheckBox(self.frame_checkbox_container)
        self.chk_math.setMinimumSize(QtCore.QSize(0, 30))
        self.chk_math.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_math.setObjectName("chk_math")
        self.verticalLayout_2.addWidget(self.chk_math)
        self.chk_punctuation = QtWidgets.QCheckBox(self.frame_checkbox_container)
        self.chk_punctuation.setMinimumSize(QtCore.QSize(0, 30))
        self.chk_punctuation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_punctuation.setObjectName("chk_punctuation")
        self.verticalLayout_2.addWidget(self.chk_punctuation)
        self.chk_special = QtWidgets.QCheckBox(self.frame_checkbox_container)
        self.chk_special.setMinimumSize(QtCore.QSize(0, 30))
        self.chk_special.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_special.setObjectName("chk_special")
        self.verticalLayout_2.addWidget(self.chk_special)
        self.chk_brackets = QtWidgets.QCheckBox(self.frame_checkbox_container)
        self.chk_brackets.setMinimumSize(QtCore.QSize(0, 30))
        self.chk_brackets.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_brackets.setObjectName("chk_brackets")
        self.verticalLayout_2.addWidget(self.chk_brackets)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame_checkbox_container)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_length = QtWidgets.QLabel(GeneratePasswordWindow)
        self.lbl_length.setObjectName("lbl_length")
        self.horizontalLayout_4.addWidget(self.lbl_length)
        self.slide_length = QtWidgets.QSlider(GeneratePasswordWindow)
        self.slide_length.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.slide_length.setMinimum(12)
        self.slide_length.setMaximum(30)
        self.slide_length.setPageStep(1)
        self.slide_length.setOrientation(QtCore.Qt.Horizontal)
        self.slide_length.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slide_length.setTickInterval(1)
        self.slide_length.setObjectName("slide_length")
        self.horizontalLayout_4.addWidget(self.slide_length)
        self.lbl_display_length = QtWidgets.QLabel(GeneratePasswordWindow)
        self.lbl_display_length.setMinimumSize(QtCore.QSize(30, 0))
        self.lbl_display_length.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_display_length.setObjectName("lbl_display_length")
        self.horizontalLayout_4.addWidget(self.lbl_display_length)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_exclude = QtWidgets.QLabel(GeneratePasswordWindow)
        self.lbl_exclude.setObjectName("lbl_exclude")
        self.horizontalLayout_3.addWidget(self.lbl_exclude)
        self.lne_exclude = QtWidgets.QLineEdit(GeneratePasswordWindow)
        self.lne_exclude.setObjectName("lne_exclude")
        self.horizontalLayout_3.addWidget(self.lne_exclude)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_generate = QtWidgets.QPushButton(GeneratePasswordWindow)
        self.btn_generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout_2.addWidget(self.btn_generate)
        self.btn_copy = QtWidgets.QPushButton(GeneratePasswordWindow)
        self.btn_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy.setObjectName("btn_copy")
        self.horizontalLayout_2.addWidget(self.btn_copy)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(GeneratePasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(GeneratePasswordWindow)

    def retranslateUi(self, GeneratePasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        GeneratePasswordWindow.setWindowTitle(_translate("GeneratePasswordWindow", "Generate Random Password"))
        self.lbl_password.setText(_translate("GeneratePasswordWindow", "Password:"))
        self.chk_uppercase.setText(_translate("GeneratePasswordWindow", "Uppercase Letters A-Z"))
        self.chk_lowercase.setText(_translate("GeneratePasswordWindow", "Lowercase Letters a-z"))
        self.chk_numbers.setText(_translate("GeneratePasswordWindow", "Numbers 0-9"))
        self.chk_math.setText(_translate("GeneratePasswordWindow", "Math Symbols + - * / ^ % ="))
        self.chk_punctuation.setText(_translate("GeneratePasswordWindow", "Punctuation . , : ; ! ? \' \" `"))
        self.chk_special.setText(_translate("GeneratePasswordWindow", "Special Characters # $ & @ ~ _ |"))
        self.chk_brackets.setText(_translate("GeneratePasswordWindow", "Brackets ( ) { } [ ] < >"))
        self.lbl_length.setText(_translate("GeneratePasswordWindow", "Length:"))
        self.lbl_display_length.setText(_translate("GeneratePasswordWindow", "1"))
        self.lbl_exclude.setText(_translate("GeneratePasswordWindow", "Exclude:"))
        self.btn_generate.setText(_translate("GeneratePasswordWindow", "Generate"))
        self.btn_copy.setText(_translate("GeneratePasswordWindow", "Copy"))
